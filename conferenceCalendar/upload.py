from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os

def upload():
    credentials_dict = {
         "type": "service_account",
        "project_id": "test-327905",
        "private_key_id": "d10b8521a4b231fadd440bf19216d46d33e28f68",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCqYJ5nkbjvL/CK\nY8gcxVzN3ePBwtKPmamFeYgHyyjPzdcLf90xiwG/fDxdIyp+0Qp749y4mGUQo9mi\nzre5TiTwCndD99ZJO/3KV4dCYFcpBrzCM1E9HO/PrGXBqh7eQYUSzUtmTqgv3IvW\nwD90X+9mmajCbqUf2u7M86uxhYPRm5/FZcx3e8rP6A+900vzNCFZwSlNM9cQ9IkX\nL/Y7rSU0S9agigC2Gm/HpuYdq8CDn31WfsdnM0VfkdzT06PpeVH6eI10Axn9zRuC\n5dQbLGbZR7peNDNRYe9NT1U4cXiKzqjTd3RjxdAAyz9L8Tmf/lFGEDay49Pe7TDW\nJr/1HSO9AgMBAAECggEAE9/zeodwOE6yU6JyLJEFU2qH8AlnAKNfOBfGO4qCd0M+\ny7OdvPLHQGwgqoi4o1SFUZByJgJ4/6jtcWWF3xLzkiDWatJVZ/OclmcBe0e7wyhr\nCohr+KIQg3xL3nyW3zxrZpcWLZgNXI/wrBt/C3dJeQGBwzSfBIlIhBYEuE+n4eKB\nl0NzquzAk2AJ32QK1j8x09FYGQKsR9GxpWpAxPujuCJZqCf1betqf/eBaX12ASeE\nl7CEhu149/Yk/m00A8RsweHkdUk28GR+NMM+q/hucqW+Vh44tT5UK2FW0YT/fCG2\niuLkrsMtRSgiv58+8IWAoSvZjuazLyzQ0LdyW89/7QKBgQDm5LdBkzV5R6BCVpwS\nKQk9rf8ggeeiQ034OiG7QznEttvdc5CgH4O0XvUhikrCLaUyXqWKXMkdx0WV3fvb\n49xpJ9G0PyM1MI34+XvvhnD45+srErkmfb7pCKJOFBmvRUbf4P5oTPoZCGBHkNdF\ncTSM71zmc2MJgVLJzmFJZsBs6wKBgQC851gVi1r+/DjCRX+MOPAeeMle3+YyxxaY\nIFUMA+w0QzyLwpooPEhLQHGyU3VesBIkr9EPhLSQW54eSg2tza07qCLnB78afiv+\nkHbNzaegEZGRiwSu4hFp7qIr+zHhRtRpZEbmVBRpX055bhV7PUXTyV+stgjf3ifY\n7oOgkoTn9wKBgHoD+dfcfFC4CjekX1u1dd2zenRqUcdM/AImbjbworGS1IOlk5Ma\ntFX4LGBqHXGZ/4ervp1sxRdIfDxjj7o3Iv4q/cXb67YrD4u4A8eja0YOARfFEDUI\nFIA/gM30D1KxMHAVDTx/GVdrNr37C9f1qAimYZii935Jaj+dIYpRk3S7AoGBAKGW\nUya6ue/72KF1yZEs81ldgQODCurMmmsu3REWGerqyNPUdwGL71tPmPItqeyBOEPh\nkTdxEPObKzpFpkXR9ildvd1aJwKGgyOSd8276XNnE9onzK27+6Fd26M7kINfjztH\n584Ghh9Mw1fj7sQouZ5cV1bpr9Wvtu49uKKWMtIpAoGAGqbQD7qxzU5rO/s7EoXD\nz/h/SPxjxZYZWET+pNYYywlamYJ7/ZWfyIjUhtfJhy4jD5ssO2FfiZ1vB9BBuPU+\nD+z/0dAvXLW5yYV5n2H9m7cr0lTYoDf+DkMN/0CQY4a5yLV826eO0l8fDleBPkOd\nBuWkuoEBk7a30PbOUYohyWE=\n-----END PRIVATE KEY-----\n",
        "client_email": "test-327905@appspot.gserviceaccount.com",
        "client_id": "118157437220557857399",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test-327905%40appspot.gserviceaccount.com"}
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_dict
    )
    client = storage.Client(credentials=credentials, project='myproject')
    bucket = client.get_bucket('mybucket')
    blob = bucket.blob('myfile')
    blob.upload_from_filename('myfile')