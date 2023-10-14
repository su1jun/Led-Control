from fastapi import APIRouter, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

my_rounter = APIRouter()
templates = Jinja2Templates(directory="templates/")

red_active = ""
green_active = ""
blue_active = ""

rad_text = ""
green_text = ""
blue_text = ""

class Pattern:
    def __init__(self):
        self.val = "^[0-9|a-z|A-Z|ㄱ-ㅎ|ㅏ-ㅣ|가-힣]*$"

pattern = Pattern()

@my_rounter.get("/", response_class=HTMLResponse)
async def index(request: Request):
    try:
        return templates.TemplateResponse("led.html", {
            "request": request,
            "color": "gray-color",
            "main_img": "gray",

            "red_active" : "",
            "green_active" : "",
            "blue_active" : "",
            "fan_active" : "",

            "rad_text" : "",
            "green_text" : "",
            "blue_text" : "",
            "gray_text" : "gray-text"
        })
    except:
        raise HTTPException(status_code=404, detail="Not found Page")

@my_rounter.get("/{color}", response_class=HTMLResponse)
async def led_load(request: Request, color : str = Path(..., title=" ")):
    if len(color) > 10:
        raise HTTPException(status_code=400, detail="request is invalid")

    if color not in ['red', 'blue', 'green']:
        raise HTTPException(status_code=400, detail="request is invalid")

    try:
        red_active = ""
        green_active = ""
        blue_active = ""

        rad_text = ""
        green_text = ""
        blue_text = ""

        main_img = color

        if color == "red":
            red_active = "active"
            rad_text = "red-text"

        elif color == "green":
            green_active = "active"
            green_text = "green-text"

        elif color == "blue":
            blue_active = "active"
            blue_text = "blue-text"

        color = str(color) + "-color"
    except:
        raise HTTPException(status_code=404, detail="Not found Page")
    
    try:
        return templates.TemplateResponse("led.html", {
            "request": request,
            "color": color,
            "main_img": main_img,

            "red_active" : red_active,
            "green_active" : green_active,
            "blue_active" : blue_active,
            "fan_active" : "",

            "rad_text" : rad_text,
            "green_text" : green_text,
            "blue_text" : blue_text,
            "gray_text" : ""
        })
    except:
        raise HTTPException(status_code=404, detail="Not found Page")

@my_rounter.get("/rs/fan", response_class=HTMLResponse)
async def led_load(request: Request):
    try:
        return templates.TemplateResponse("fan.html", {
            "request": request,
            "color": "gray-color",
            "main_img": "fan",

            "red_active" : "",
            "green_active" : "",
            "blue_active" : "",
            "fan_active" : "active",

            "rad_text" : "",
            "green_text" : "",
            "blue_text" : "",
            "gray_text" : "gray-text"
        })
    except:
        raise HTTPException(status_code=404, detail="Not found Page")
    