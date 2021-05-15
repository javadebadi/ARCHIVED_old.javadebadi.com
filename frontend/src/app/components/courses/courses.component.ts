import { Component, OnInit } from '@angular/core';
import { CoursesService } from '../../services/courses.service';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.scss']
})
export class CoursesComponent implements OnInit {

  courses: any[] = [];
  constructor(
    private coursesService: CoursesService
  ) { }

  ngOnInit(): void {
    const variable = this.coursesService.getCourses().subscribe(x => console.log(x));
  }

}
