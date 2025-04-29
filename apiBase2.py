from playwright.sync_api import Playwright

orderspayload={"orders":[{"country":"India","productOrderedId":"6581cade9fd99c85e8ee7ff5"}]}

class APIUtils:

    def getToken(self, playwright:Playwright,user_credetials):
        username=user_credetials['user_email']
        password=user_credetials['user_password']
        Api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=Api_request_context.post("/api/ecom/auth/login", data={"userEmail":username,"userPassword":password})
        assert response.ok
        print(response.json())
        responseBody=response.json()
        return responseBody["token"]

    def createOrder(self,playwright:Playwright,user_credetials):
        token=self.getToken(playwright,user_credetials)
        Api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = Api_request_context.post("/api/ecom/order/create-order",
                                            data=orderspayload,
                                            headers={"authorization":token, "content-type":"application/json"})
        print(response.json())
        response_Body =response.json()
        orderId= response_Body["orders"][0]
        return orderId