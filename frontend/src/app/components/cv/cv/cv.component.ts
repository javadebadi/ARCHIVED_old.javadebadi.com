import { Component, OnInit } from '@angular/core';
import { CVService } from 'src/app/services/cv.service';

@Component({
  selector: 'app-cv',
  templateUrl: './cv.component.html',
  styleUrls: ['./cv.component.scss']
})
export class CvComponent implements OnInit {

  educations: any;
  constructor(
    private cvService: CVService
  ) { }

  ngOnInit(): void {
    this.cvService.getEducation().subscribe(educations => this.educations = educations);
  }



}
