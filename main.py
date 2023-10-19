from fastapi import Response
import requests
import os
import random
import uvicorn
from fastapi import Request
import json
from user_agent import generate_user_agent
from fastapi.responses import JSONResponse
from fastapi import FastAPI
import secrets
cok = secrets.token_hex(8) * 2
app = FastAPI()
a=int(0)
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get('/api/gmail/v1/v.1/{gmail}')
async def ga(gmail: str, request: Request):
    client_host = request.client.host
    global a,tl,cok
    fi =  open('token.txt','r').read().splitlines()
    try:

        tl =  random.choice(fi)
    except :
        url1 ='https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=81859&rt=j'
        headers ={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Length': '2064',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': cok,#'OTZ=7108643_44_44__44_; SID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmr15yp_oaL_xeeEfBVgjaBw.; __Secure-1PSID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmCBuWPmTPTNYW2baZrFNzSg.; __Secure-3PSID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmIpBbJ-F4oxIaIpyA8uiYoA.; HSID=AC7zuP_2Cfr6WV4Wo; SSID=Ad8QrA6AwPbt0I4Ct; APISID=AcEUObc0anVhu-iW/AfERzaprKwiLXOZdQ; SAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; __Secure-1PAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; __Secure-3PAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; ACCOUNT_CHOOSER=AFx_qI50RgWS2YPtrRsLg5jdWUSb4etOkTUEDsCovfewzH7R2eHUxsbxIQlKQ3WhhWXY4b6FvxZRxr8f9jBG3F-jqyF63uOAW-aRViL0ebgO0SVvTY2qy2A; LSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEslG00ghU8D3fbQuCtqoctP1Q.; __Host-1PLSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEslCCZcErElgJT2GDIldS5yLA.; __Host-3PLSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEsl-v0Slnxtri4P9Pfc4GyQdw.; SEARCH_SAMESITE=CgQI55gB; AEC=Ad49MVHZHQnKsQr1I69z0bbuXdrGfmBK65sFxqCVzpjtiInm7RCL0-x0fao; 1P_JAR=2023-07-22-09; NID=511=TzSyzIQPm-iT9JvsSke0UtNiC-D4T9Pxwaju7i18lmOW5TQYCGPdgsK1bNzeSX4sgQQqPSxhNEO70WLgSS-e8yExlc6apcS7llKLVJfi2ojviDNZkS56nZ7A5tBEeLUZyyk67wCuqnvGNnxfcrEzkhbnZyFr7LjaptoAun37vzTRxc7sDIRXQgYelYKHeDA4sydYNavUj8-2aIeluThJFZzVOtNUvm_pmB8Hl186NrVh-Ic-ZvgIcycFoXlWSzWWM0axLdiEkvoaueDhjw; __Secure-1PSIDTS=sidts-CjEBPu3jIYr-PGBP-nzKbXTJetKPgsUr4wHSMBKn3VT0Q0f8RiGe-IPjQJ5UmAYADiFvEAA; __Secure-3PSIDTS=sidts-CjEBPu3jIYr-PGBP-nzKbXTJetKPgsUr4wHSMBKn3VT0Q0f8RiGe-IPjQJ5UmAYADiFvEAA; __Host-GAPS=1:8pTs3fQUZi0PSARTUgKu0XQD7uTV2V70VDF8CCsojS0dlIRhSoNmFfZQNTyUyS4dLDyN6ooBCMpAbKh3LY3_MCD7VaxOjw:8YgpjTOK8955x5s0; SIDCC=APoG2W-kcNEPTAYb39TL2fO8qnBvjAXylVVDzCnQZWO5CyeGbPeHT_s59jfWE1WR-lOae4sBYqI; __Secure-1PSIDCC=APoG2W8N4c7gP3G-DWVqhS2gfO_IbSUR5YZeCPzxnYL4bGlX6HWq4YgQuAeUQaJ29-ausVXYQg; __Secure-3PSIDCC=APoG2W-1HlpLmTDjKURgPV16ED3Ryb4kQbTo-MSWiOf2Kewy1tmjtoTVtZjnKPr8RYT6ldCV2AU',
            'Google-Accounts-Xsrf': '1',
            'Origin': 'https://accounts.google.com',
            'Referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fe-11-8976fbef68f7663ea60e661c4f9b5-1475984d740df90158840a19af1784235fe51b7e&flowName=GlifWebSignIn&flowEntry=SignUp',
            'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'Sec-Ch-Ua-Arch': '"x86"',
            'Sec-Ch-Ua-Bitness': '"64"',
            'Sec-Ch-Ua-Full-Version': '"114.0.5735.199"',
            'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Model': '""',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
            'Sec-Ch-Ua-Wow64': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'X-Chrome-Id-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fbc22924-4987-44e1-b323-7d3efd00dded,signin_mode=all_accounts,signout_mode=show_confirmation',
            'X-Client-Data': 'CIm2yQEIprbJAQipncoBCIXwygEIlKHLAQiFoM0BCJyrzQEI2rTNAQjcvc0BCLy+zQEI1L7NAQjgxM0BCO/EzQEIqMXNAQ==',

            'X-Same-Domain': '1'


            }
        data1 ={
            'continue': 'https://accounts.google.com/ManageAccount?nc=1',
            'f.req': '["AEThLlzCTLyoshyixCRoA6ccDmpMOZ-PomPBC9ByGLX3o8xDU8VIGoGBy9vj5D-3txgufFW3ZtNzDWAvNXmveIo95oRGruoTaALFrDIhPuzD6SscTf--ya7mjnd2vNDxwPxgQ8x0xH0lZbKjF_sEWyzM-yiKQQMUpjq4lV_UmC87yQkt9qmndf-Jw-HrXgdPSNZYSfnvTk-u",null,null,null,null,0,0,"zaid","zaid","web-glif-signup",0,null,10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],1]',
            'at': 'AFoagUUm6HX36QVWDo2X-TVlmW9vQ8p6Iw:1689946784467',
            'azt': 'AFoagUWbi-h35AWa309jmxoLN8DKwbn2KA:1689946784467',
            'cookiesDisabled': 'false',
            'deviceinfo':' [null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
            'gmscoreversion': 'undefined',
            'flowName': 'GlifWebSignIn',
            'checkConnection': 'youtube:584:0',
            'checkedDomains': 'youtube',
            'pstMsg': '1'

        }
        print("wait..")
        for iii in range(2):

            rt=  requests.post(url1,headers=headers,data=data1).text
            print(rt)
            ope =  len(open('token.txt','r').readlines())

            tp =  rt.split('"gf.ttu",null,"')[1].split('"]')[0]
            with open('token.txt','a') as f0:
                f0.write(f'{tp}\n')
            fi =  random.choice(tl)

    print(fi)

    gmail1 = gmail
    number = '1234567890'
    print(tl)


        #num = str(''.join(random.choice(number) for i in range(7)))
    url = f'https://accounts.google.com/_/signup/usernameavailability?hl=ar&TL={fi}&_reqid=481859&rt=j'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Length': '1146',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        #'Cookie': 'OTZ=7108643_44_44__44_; 1P_JAR=2023-07-20-14; AEC=Ad49MVGLdm0yAKYn0PndzTaQZB5QDYm_tDCKH_vF7CBNWRHo9k-MLgX6Qpg; NID=511=eT6Dsn5OeQnzWAsknlkrcehUjeWJExuQWLkRMewKpYeYl8vXZfgYED18YKlywX6u--ceLMVOrRfJ69SuyDP3o42HRRA6Xqlcetwi2-XribhN2gI83vbhqXf_3Wwe8jB_XYR7Bt8qrw4nez5AeZ_rcdSLWVAqT1i-RC3yUoeJumU6MzZqAlDF2efOAFLXovoqF2RHW6sZwqZt-8s; __Host-GAPS=1:8Wx3cVdfKlC-Is1UIC_sktz1J0GrkA:upvwVYNk8jYTFOXH',
        'Google-Accounts-Xsrf': '1',
        'Origin': 'https://accounts.google.com',
        'Referer':
        'https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=SignUp&TL=AJvNCbbAigRHG5Ypddwgp39mKdyniOE3D3uLi3iK805IzUq1NNSbRnz7QQ6b_tTu',
        'User-Agent': generate_user_agent(),
        #'X-Chrome-Id-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=0e886cd5-0c72-4d02-adb8-aa64ae664a4a,signin_mode=all_accounts,signout_mode=show_confirmation',
        #'X-Client-Data': 'CIm2yQEIprbJAQipncoBCIXwygEIlqHLAQiFoM0BCJyrzQEI2rTNAQjcvc0BCLy+zQEI1L7NAQj/v80BCLLDzQEI7sTNAQioxc0B'
    }
    data = {
        'datcontinue': 'https://uc.appengine.google.com/_ah/conflogin?state=~AJKiYcGoPiLJb7FyAN6mbCNCjMH037vL_6C39BUsJA2GF6P5lw1fJ6zYEHHUw663dDmmWQqnSQj6F1H89kr0oAzGCTf1OVJVmr9O71L1w89w388Qo8F51B0AsXfY4lW59yc42hfwocycpD-KrQxXpL_wNY1CXqq7EwVgxTdIeLOVnU-5xSbZ8812E9pDOYWDOi2xFjrP52ODHXY16KTZWlHmcwb4WPbjByt1nT71cz8msPMP1rVSoXY',
        'dsh': 'S2080850673:1689863726476816',
        'flowEntry': 'ServiceLogin',
        'ifkv': 'AeDOFXgxTTjgoRCMuYvMYScwDmQo7816fmgZo5HW-2qv1sxmBtxR8_QpcokS3oMTn4QP3Fp_J3h15Q',
        'f.req': '["TL:{}","{}",0,0,1]'.format(tl, gmail1),
        'azt': 'AFoagUWjPq1xG8LVoJkd3pOHgMJrOj0MAA:1689863743434',
        'cookiesDisabled': 'false',
        'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
        'gmscoreversion': 'undefined',
        'flowName': 'GlifWebSignIn',
        'checkConnection': 'youtube:452:0',
        'checkedDomains': 'youtube',
        'pstMsg': '1',
    }

    req = requests.post(url, headers=headers, data=data).text
    print(req)
    if ('"gf.uar",1') in req:

        fa = 'True'
        daa1 = {
            'status': 'Ok',
            'email': gmail1+'@gmail.com',
            'ar': 'متاح',

            'py': 'zaid kareem',
            'telegram': '@zaidkarrem - https://t.me/BBMZZ',
            'ip': client_host
        }
        return JSONResponse(content=daa1)

    elif ('78') in req:
        ln = open('token.txt', 'r').read().splitlines()
        if tl in ln:
            with open("token.txt", "r") as f:
                lines = f.readlines()
                with open("token.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != "{}".format(tl):
                            f.write(line)
                        print('ok')
                    url1 ='https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=81859&rt=j'
                    headers ={
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Content-Length': '2064',
                        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                        'Cookie': cok,#'OTZ=7108643_44_44__44_; SID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmr15yp_oaL_xeeEfBVgjaBw.; __Secure-1PSID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmCBuWPmTPTNYW2baZrFNzSg.; __Secure-3PSID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmIpBbJ-F4oxIaIpyA8uiYoA.; HSID=AC7zuP_2Cfr6WV4Wo; SSID=Ad8QrA6AwPbt0I4Ct; APISID=AcEUObc0anVhu-iW/AfERzaprKwiLXOZdQ; SAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; __Secure-1PAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; __Secure-3PAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; ACCOUNT_CHOOSER=AFx_qI50RgWS2YPtrRsLg5jdWUSb4etOkTUEDsCovfewzH7R2eHUxsbxIQlKQ3WhhWXY4b6FvxZRxr8f9jBG3F-jqyF63uOAW-aRViL0ebgO0SVvTY2qy2A; LSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEslG00ghU8D3fbQuCtqoctP1Q.; __Host-1PLSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEslCCZcErElgJT2GDIldS5yLA.; __Host-3PLSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEsl-v0Slnxtri4P9Pfc4GyQdw.; SEARCH_SAMESITE=CgQI55gB; AEC=Ad49MVHZHQnKsQr1I69z0bbuXdrGfmBK65sFxqCVzpjtiInm7RCL0-x0fao; 1P_JAR=2023-07-22-09; NID=511=TzSyzIQPm-iT9JvsSke0UtNiC-D4T9Pxwaju7i18lmOW5TQYCGPdgsK1bNzeSX4sgQQqPSxhNEO70WLgSS-e8yExlc6apcS7llKLVJfi2ojviDNZkS56nZ7A5tBEeLUZyyk67wCuqnvGNnxfcrEzkhbnZyFr7LjaptoAun37vzTRxc7sDIRXQgYelYKHeDA4sydYNavUj8-2aIeluThJFZzVOtNUvm_pmB8Hl186NrVh-Ic-ZvgIcycFoXlWSzWWM0axLdiEkvoaueDhjw; __Secure-1PSIDTS=sidts-CjEBPu3jIYr-PGBP-nzKbXTJetKPgsUr4wHSMBKn3VT0Q0f8RiGe-IPjQJ5UmAYADiFvEAA; __Secure-3PSIDTS=sidts-CjEBPu3jIYr-PGBP-nzKbXTJetKPgsUr4wHSMBKn3VT0Q0f8RiGe-IPjQJ5UmAYADiFvEAA; __Host-GAPS=1:8pTs3fQUZi0PSARTUgKu0XQD7uTV2V70VDF8CCsojS0dlIRhSoNmFfZQNTyUyS4dLDyN6ooBCMpAbKh3LY3_MCD7VaxOjw:8YgpjTOK8955x5s0; SIDCC=APoG2W-kcNEPTAYb39TL2fO8qnBvjAXylVVDzCnQZWO5CyeGbPeHT_s59jfWE1WR-lOae4sBYqI; __Secure-1PSIDCC=APoG2W8N4c7gP3G-DWVqhS2gfO_IbSUR5YZeCPzxnYL4bGlX6HWq4YgQuAeUQaJ29-ausVXYQg; __Secure-3PSIDCC=APoG2W-1HlpLmTDjKURgPV16ED3Ryb4kQbTo-MSWiOf2Kewy1tmjtoTVtZjnKPr8RYT6ldCV2AU',
                        'Google-Accounts-Xsrf': '1',
                        'Origin': 'https://accounts.google.com',
                        'Referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fe-11-8976fbef68f7663ea60e661c4f9b5-1475984d740df90158840a19af1784235fe51b7e&flowName=GlifWebSignIn&flowEntry=SignUp',
                        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                        'Sec-Ch-Ua-Arch': '"x86"',
                        'Sec-Ch-Ua-Bitness': '"64"',
                        'Sec-Ch-Ua-Full-Version': '"114.0.5735.199"',
                        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
                        'Sec-Ch-Ua-Mobile': '?0',
                        'Sec-Ch-Ua-Model': '""',
                        'Sec-Ch-Ua-Platform': '"Windows"',
                        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
                        'Sec-Ch-Ua-Wow64': '?0',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                        'X-Chrome-Id-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fbc22924-4987-44e1-b323-7d3efd00dded,signin_mode=all_accounts,signout_mode=show_confirmation',
                        'X-Client-Data': 'CIm2yQEIprbJAQipncoBCIXwygEIlKHLAQiFoM0BCJyrzQEI2rTNAQjcvc0BCLy+zQEI1L7NAQjgxM0BCO/EzQEIqMXNAQ==',

                        'X-Same-Domain': '1'


                        }
                    data1 ={
                        'continue': 'https://accounts.google.com/ManageAccount?nc=1',
                        'f.req': '["AEThLlzCTLyoshyixCRoA6ccDmpMOZ-PomPBC9ByGLX3o8xDU8VIGoGBy9vj5D-3txgufFW3ZtNzDWAvNXmveIo95oRGruoTaALFrDIhPuzD6SscTf--ya7mjnd2vNDxwPxgQ8x0xH0lZbKjF_sEWyzM-yiKQQMUpjq4lV_UmC87yQkt9qmndf-Jw-HrXgdPSNZYSfnvTk-u",null,null,null,null,0,0,"zaid","zaid","web-glif-signup",0,null,10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],1]',
                        'at': 'AFoagUUm6HX36QVWDo2X-TVlmW9vQ8p6Iw:1689946784467',
                        'azt': 'AFoagUWbi-h35AWa309jmxoLN8DKwbn2KA:1689946784467',
                        'cookiesDisabled': 'false',
                        'deviceinfo':' [null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
                        'gmscoreversion': 'undefined',
                        'flowName': 'GlifWebSignIn',
                        'checkConnection': 'youtube:584:0',
                        'checkedDomains': 'youtube',
                        'pstMsg': '1'

                    }
                    print("wait..")
                    for iii in range(2):

                        rt=requests.post(url1,headers=headers,data=data1).text
                        print(rt)
                        ope = len(open('token.txt','r').readlines())

                        tp = rt.split('"gf.ttu",null,"')[1].split('"]')[0]
                        with open('token.txt','a') as f0:
                            f0.write(f'{tp}\n')
            #tl=random.choice(fi)
            #tl=tl





    else:
        fa = 'False'
        data2 ={
            'status': 'Bad',
            'email': gmail1+'@gmail.com',

            'ar': 'غير متاح',
            'py': 'zaid kareem',
            'telegram': '@zaidkarrem - https://t.me/BBMZZ',
            'ip': client_host
        }
        return JSONResponse(content=data2)
        #jsonn = json.dumps(daa, indent=4, default=)
        #return Response(content=jsonn, media_type='application/json')

uvicorn.run(app,host='0.0.0.0',port=8080)