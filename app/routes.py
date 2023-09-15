from fastapi import APIRouter, Request, HTTPException, Depends

from app.settings import TENANT_ROUTING
from app.app import app
from app.libs.mongoclient import client

def adminCheck(request: Request):
    # if request.client.host not in admin_access_whiteList and "0.0.0.0" not in admin_access_whiteList:
    #     raise HTTPException(status_code=403, detail="Forbidden")
    return True

# def adminCheckLoggedIn(request: Request, Authorize: AuthJWT = Depends()):
#     # if request.client.host not in admin_access_whiteList and "0.0.0.0" not in admin_access_whiteList:
#     #     raise HTTPException(status_code=403, detail="Forbidden")
    
#     try:
#         claims = Authorize.get_raw_jwt()

#         if redisCheck(claims['jti']):
#             raise HTTPException(status_code=401, detail="Unauthorized")
        
#         print(claims)
#         if claims['type'] != "confidential" and claims['otpVerified'] != True:
#             raise HTTPException(status_code=401, detail="Unauthorized")
        
#     except Exception as e:
#         raise HTTPException(status_code=401, detail="Unauthorized")
    
    
if TENANT_ROUTING == "subdomain":
    prefix = "/admin"
elif TENANT_ROUTING == "path":
    prefix = "/{tenant}/admin"

def database_exists(db_name):
    db_list = client.list_database_names()
    if db_name in db_list:
        print(f"The database '{db_name}' exists.")
        return True
    else:
        print(f"The database '{db_name}' does not exist.")
        return False
  
def getTenantInfo(request: Request):
    if TENANT_ROUTING == "subdomain":
        tenant = request.headers["host"].split(".")[0]
    elif TENANT_ROUTING == "path":
        tenant = request.url.path.split("/")[1]
    else:
        raise HTTPException(status_code=404, detail="Tenant routing not configured")
    # db.execute(text("SET search_path TO 'public'"))
    tenantInfo=database_exists(tenant)

    if tenantInfo == False:
        raise HTTPException(status_code=404, detail={
            "message": "Tenant not found",
            "status_code": 404
        })
    else:
        return {"tenant": tenant, "tenantInfo": tenantInfo}    


adminAppRouter = APIRouter(

    prefix="/admin",
    tags=["adminAuth"],
    dependencies= [Depends(adminCheck)]
 )

# adminDashboardRouter = APIRouter(
#     prefix="/admin/dashboard",
#     tags=["adminDashboard"],
#     # dependencies= [Depends(adminCheck), Depends(adminCheckLoggedIn)]
# )



# tenantAppRouter = APIRouter(
#     prefix=prefix,
#     tags=["tenant"])


tenantDashboardRouter = APIRouter(
    prefix=prefix+"/dashboard",
    tags=["tenantDashboard"],
  
    )



seekerAppRouter = APIRouter(
    prefix="/seeker",
)

seekerDashboardRouter = APIRouter(
    prefix="/seeker/dashboard",
)

