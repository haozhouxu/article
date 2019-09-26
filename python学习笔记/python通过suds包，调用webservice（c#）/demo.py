from suds.client import Client
import base64

def test_suds():
    webservice_url = "http:localhost:8478/DataService.asmx?wsdl"

    client = Client(webservice_url)

    # 查看service提供的方法

    # 调用参数为string的方法
    result = client.service.GetString("demo")
    print(result)

    # 调用参数为：string，byte[]的方法
    file_path = r"c:\demo01.pdf"
    with open(file_path, mode="rb") as f:
        content = base64.b64encode(f.read()).decode("utf-8")

        result = client.service.UploadFile("demo01",content)
        print(result)