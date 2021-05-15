import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from './../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CVService {

  constructor(
    private http: HttpClient
  ) { }

  getCV(): Observable<any[]> {
    return this.http.get<any[]>(environment.cvURL);
  }

  getDegrees(): Observable<any[]>{
    return this.http.get<any[]>(environment.degreesURL);
  }

  getEducation(): Observable<any[]>{
    return this.http.get<any[]>(environment.educationURL);
  }

}
