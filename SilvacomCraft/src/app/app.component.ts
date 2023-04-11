import { Component } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'SilvacomCraft';

  // emtpy weather json object to be set
  weather: any ={
    "location": {
        "name": "",
        "country": "",
        "localtime": ""
    },
    "current": {
        "temp_c": 0,
        "temp_f": 0,
        "is_day": 1,
        "condition": {
            "text": "",
            "icon": "",
            "code": 1003
        }
    }
  }

  info: any;
  Cities: any = []
  rootURL = 'http://127.0.0.1:5000/';
  apiKey = '76b8ebdad54f4237b4144217231004'

  constructor(private http: HttpClient) { }

  // setting the city selected from drop down
  selectedCity = this.Cities;
  
  // makes call to backend Flask api
  // params: the city label (ei. "Venice") 
  // returns: the http get response
  weatherApiCall(cityName:string): Observable<any> {
    let queryParams = new HttpParams();
    queryParams = queryParams.append("cityName", cityName)
    return this.http.get(this.rootURL+"/weather/"+cityName)
  }

  // get weather data from api call and saves response json info to this.weather object
  // params: selected city object 
  // returns: the http get response
  getWeather(city:any) {
    console.log("Getting the Weather for:"+city.label)
    this.weatherApiCall(city.label).subscribe((response) => {
      console.log("response received")
      this.weather=response
      console.log(this.weather)
    })
  }

  // makes call to backend Flask api
  // returns: the http get response
  getCities(): Observable<any> {
    return this.http.get(this.rootURL+"/cities")
  }

  // gets city list from Flask backend
  // sets this.City to list recieved 
  ngOnInit() {
    this.getCities().subscribe((response) => {
      console.log("response received")
      this.info=response
      this.Cities=this.info.Cities
    })
  }
}

  

