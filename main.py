
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from sbt_project import app_config, app_logger
from sbt_project.main import run
from sbt_project.common.exception import CustomException, InternalServerError


# FastAPI app
app = FastAPI()

# TODO : CORS 등록
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# add api router
# app.include_router(crew.router)
# app.include_router(material.router)
# app.include_router(quest.router)
# app.include_router(user.router)


# add exception manager
@app.exception_handler(CustomException)
async def exception_handler(request: Request, ex: CustomException):
    app_logger.error(f'[{request.method}] {request.url}: {request.client.host}:{request.client.port}')
    return JSONResponse(status_code=ex.status_code, content=ex.detail)



@app.get("/run")
async def run_crewai():
    try:
        result = run()
        return {"status": "success", "result": result}
    except InternalServerError as ex:
        return JSONResponse(status_code=ex.status_code, content=ex.detail)



if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=5000, reload=app_config.app_reload)

# def main():
#     print("Hello from sbt-project!")
#
# if __name__ == "__main__":
#     main()
