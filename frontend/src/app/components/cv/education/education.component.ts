import { Component, OnInit } from '@angular/core';
import { CVService } from '../../../services/cv.service';

@Component({
  selector: 'app-education',
  templateUrl: './education.component.html',
  styleUrls: ['./education.component.scss']
})
export class EducationComponent implements OnInit {

  educations: any;
  
  constructor(
    private cvService: CVService
  ) { }

  ngOnInit(): void {
    this.cvService.getEducation().subscribe(educations => this.educations = educations);
  }

}
