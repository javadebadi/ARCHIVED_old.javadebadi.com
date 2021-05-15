import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from './../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CoursesService {

  private coursesURL = environment.apiURL + "courses/";
  constructor(
    private http: HttpClient
  ) { }

  /** GET courses from the server */
  getCourses(): Observable<any[]> {
    return this.http.get<any[]>(this.coursesURL);
  }

}
