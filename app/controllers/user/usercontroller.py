import random
from app.app import app
from fastapi import Depends, Response,HTTPException
from fastapi import FastAPI
import hashlib
from app.libs.authJWT import * 
from app.schemas.user.userschema import usersignup,userLoginSchema,emailVerifyOtpSchema,ForgotPasswordSchema
from datetime import datetime, timedelta
from app.libs.msg91Email import sendmail   

from app.libs.mongoclient import user_collection
# from app.tpls.smsTpls import sendOtpTpl
from bson import ObjectId


@app.post("/users/")
async def createuser(user:usersignup,Authorize:AuthJWT=Depends()):
    user_dict=user.dict()
    data=user_collection.find_one({"Name":user.name})
    if data:
        return{
            "status_code":200,
            "message":"user already exist"
        }
    print(user)
    access_token = Authorize.create_access_token(subject=str(data['_id']), expires_time=6048000, 
                                    
                user_claims= {
                        "data":user.name,
                    })        
    user_collection.insert_one(user_dict)
    return {
        
       "status_code":200,
       "message":"user added successfuly"
   }  
@app.post("/login/")
async def login(studentlogin:userLoginSchema,Authorize:AuthJWT=Depends()):
    user_dict=studentlogin.dict()
    email=user_collection.find_one({"$and":[{"email":studentlogin.email}, {"password":studentlogin.password}]})
    if email: 
        access_token = Authorize.create_access_token(subject=str(email['_id']), expires_time=6048000, 
                                    
                user_claims= {
                        "email":studentlogin.email,
                    })        
        return {"status_code": 200,
                    "message": "Login successfully",
                    "access_token": access_token,} 
    else:
        return{
            "status_code":400,
            "message":"invalid details"
        }
@app.post("/forgot-password/")
async def forgot_password(forgot_password: ForgotPasswordSchema,Authorize:AuthJWT=Depends()):
    email = forgot_password.email
    user_data = user_collection.find_one({"email": email})

    otp = random.randint(100000, 999999)
    res = user_collection.update_one({"_id": user_data['_id']}, {
                                   "$set": {"mobileOtp": otp, "mobileOtpCreatedAt": datetime.now()}})
        # sendsms(user['mobile'], sendOtpTpl(otp))
    print(user_data['email'])
    emailsent=sendmail(user_data['email'],"IKEA","info@gmail.com","otp","you OTp for login is "+str(otp))
        # sendmail("vikas50572kushwaha@gmail.com", 'Vikas Kushwaha', 'info@koneqto.com', 'Test Subject', 'This is a test body'+str(otp))
    print(emailsent)
    access_token = Authorize.create_access_token(subject=str(user_data['_id']),
                                                     user_claims={

            "type": "confidential",
            "otpVerified": False,
            "forgotPassword": True
        }
        )

    return HTTPException(status_code=200, detail={
            "status_code": 200,
            "message": "User found",
            "access_token": access_token

        })

@app.post("/verifyOtp")
def verify_otp(response: Response, otp: emailVerifyOtpSchema, Authorize: AuthJWT = Depends()):
    user_id = Authorize.get_jwt_subject()
    user_data = user_collection.find_one({"_id": ObjectId(user_id)})
    print(user_data)
    
    if user_data:
        if user_data['mobileOtp'] == otp.otp:
         return {
            "status":200,
            "message": "OTP verified successfully"
            }
        else:
            return{
                "message":list(otp),
                "message":"OTP verified successfully"
            }
    else:
        return{
            "status_code":400, "message":"Invalid OTP"
        }