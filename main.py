from app.app import app
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.user.userschema import usersignup,userLoginSchema,emailVerifyOtpSchema,ForgotPasswordSchema

# from app.models.admin import skillsAndSponsersModels
# from app.models.admin import servicesModel
# from app.models.tenant import tenantModel
# from app.models.admin import adminWorkspaceAssessmentModel
# from app.models.admin import adminQuestionbankModel
# from app.routes import adminAppRouter, adminDashboardRouter,tenantAppRouter,tenantDashboardRouter,seekerAppRouter,seekerDashboardRouter
# from app.controllers.tenant import tenantRegistrationController,tenantAuthControllers,tenantUsermanagement,candidateController,tenantWorkspaceController,examControllerNewSchem,tenantDashboardController,newQuestionController,sectionController
# from app.controllers.tenant import  tenanatSponserController,tenantSkillsController,tennatAssessmentController,tenantQuestionController,proctoringController,tenantBatchController,emailTemplateController,showAllAdminAssessmentController,newExamController
# from app.controllers.admin import adminAuthController,adminDashboardController, adminSkillQuestionBankController,servicesController,adminPaymentsController,adminQuestionControllers,paymentGatewayControllers,adminSkillQuestionController
# from app.controllers.admin import adminUserMgtController,adminTenantController,adminSkillController,adminSponserController,adminAssessmentController,adminWorkspaceController,sectionController
# from app.controllers.seeker import seekerAuthController,seekerDashboardController
from app.controllers.user import usercontroller

# from app.controllers.tenant import tenantAuthController
# from app.controllers.seeker import report
# adminQuestionbankModel.Base.metadata.create_all(bind=engine)
# paymentAdminModel.Base.metadata.create_all(bind=engine)
# servicesModel.Base.metadata.create_all(bind=engine)
# tenantModel.Base.metadata.create_all(bind=engine)
# adminWorkspaceAssessmentModel.Base.metadata.create_all(bind=engine)
# adminAssessmentModel.Base.metadata.create_all(bind=engine)
# skillsAndSponsersModel.Base.metadata.create_all(bind=engine)
# adminWorkspaceAssessmentModel.Base.metadata.create_all(bind=engine)

import os
# app.include_router(tenantAppRouter)
# app.include_router(tenantDashboardRouter)
# adminApp.include_router(adminAppRouter)
# adminApp.include_router(adminDashboardRouter)
# adminApp.include_router(seekerAppRouter)
# adminApp.include_router(seekerDashboardRouter)

import os
# adminApp.include_router(tenantAppRouter)
# adminApp.include_router(tenantDashboardRouter)
# adminApp.include_router(adminAppRouter)
# adminApp.include_router(adminDashboardRouter)
# adminApp.include_router(seekerAppRouter)
# adminApp.include_router(seekerDashboardRouter)

# origins = ["http://localhost:3000","http://localhost:3001","https://trovenfe.smartinternz.com","http://stackdef.localhost:3000",
#            "http://stack.localhost:3001","http://192.168.1.102","http://192.168.68.93:3000","http://192.168.68.189:3000",
#            "http://192.168.68.55:3000","https://trovenapi.smartinternz.com","https://stack.trovenfe.smartinternz.com",
#            "http://stack.trovenfe.smartinternz.com","http://192.168.68.58:3000","http://192.168.68.63","http://192.168.68.61",
#            "https://def.trovenfe.smartinternz.com","http://def.localhost:3000","http://192.168.68.201:3000",
#            "https://stackdef.trovenfe.smartinternz.com","http://smartbridge.trovenfe.smartinternz.com","http://stackdef.localhost:3000",
#            "https://smartbridge.trovenfe.smartinternz.com"]


        
        
origins=["https://trovenfe.smartinternz.com","http://localhost:3000","http://192.168.68.59:3000","http://mysort.localhost:3000","http://192.168.68.69:3000","http://192.168.68.60:3000","http://192.168.1.35:3000","http://stack.192.168.68.60:3000","http://192.168.29.250:8000","http://192.168.29.250:8080"]
def print_string_in_file(file_path):
    CORS=[]
    try:
        with open(file_path, 'r') as file:
            for line in file:
                    # print(f"String  found in the file!")
                    CORS.append(line.split("\n")[0])
            for i in CORS:
                origins.append("https://"+i+".trovenfe.smartinternz.com")
                origins.append("http://"+i+".localhost:3000")
                origins.append("http://"+i+".192.168.68.59:3000")
                origins.append("http://"+i+".localhost:3001")
                origins.append("http://"+i+".192.168.29.250:8000") 
                origins.append("https://"+1+".192.168.29.250:8080")  
    except IOError:
        print(f"Error: Unable to open file '{file_path}'")


path = os. getcwd() + '/app/utills/companySortnames.txt'

print_string_in_file(path)
        
# print(origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @adminApp.post("/")
# def create_user(prompt: oaiPrompt):
#     prompt2jsonQA = """generate {0} mcq questions on {1} with answers 
#     in JSON format. label type as code if question have code sample. 
#     add question complexity as questionLevel in json""".format(5, prompt.prompt)
#     completion = openaiClient(prompt2jsonQA)
#     jsonData = completion.choices[0].text.replace("\n", "")
#     print(jsonData)
#     try:
#         jsonData = json.loads(jsonData)
#     except json.decoder.JSONDecodeError as e:
#         print(e)
#     return jsonData 

# @adminApp.post("/getSkills")
# def get_skills(prompt: oaiPrompt):
#     prompt2jsonQA = """Create json out for required skills to become {0}, seperate skills by categories """.format(prompt.prompt)
#     completion = openaiClient(prompt2jsonQA)
#     jsonData = completion.choices[0].text.replace("\n", "")
#     print(jsonData)
#     try:
#         jsonData = json.loads(jsonData)
#     except json.decoder.JSONDecodeError as e:
#         print(e)
#     return jsonData

# @adminApp.post("/getTasks")
# def get_skills(prompt: oaiPrompt):
#     prompt2jsonQA = """Create json output consisting of  """.format(prompt.prompt)
#     completion = openaiClient(prompt2jsonQA)
#     jsonData = completion.choices[0].text.replace("\n", "")
#     print(jsonData)
#     try:
#         jsonData = json.loads(jsonData)
#     except json.decoder.JSONDecodeError as e:
#         print(e)
#     return jsonData

# @adminApp.post("/validate")
# def get_skills(prompt: oaiPrompt):
#     prompt2jsonQA = """give output in json format consisting of explanation as 'Explanation' and marks as 'Marks' on scale of 10 by validating give content as {} teacher. 
#      If overall statement or context is wrong make score zero. marks can be float. answer should fit the given question. 
#     given question for user is "What is a database designing, explain with example ?", and user answer is {} """.format("strict",prompt.prompt)
#     completion = openaiClient(prompt2jsonQA)
#     jsonData = completion.choices[0].text.replace("\n", "")
#     print(jsonData)
#     try:
#         jsonData = json.loads(jsonData)
#     except json.decoder.JSONDecodeError as e:
#         print(e)
#     return jsonData