import { Component, OnInit } from '@angular/core';
import { HardDataService } from '../../services/hard-data.service';

@Component({
  selector: 'app-header-image',
  templateUrl: './header-image.component.html',
  styleUrls: ['./header-image.component.scss']
})
export class HeaderImageComponent implements OnInit {
  hardData: any;
  personalData: any;
  fullName: string = "";
  jobTitle: string = "";
  jobSubject: string = "";
  imagePath: string = "";

  constructor(
    private hardDataService: HardDataService
  ) { }

  ngOnInit(): void {
    this.getHardData();
  }

  getHardData(): void {
    this.hardDataService.getHardData()
      .subscribe(hardData => this.hardData = hardData);
    this.personalData = this.hardData.personal_info;
    this.fullName = this.personalData["full_name"];
    this.jobTitle = this.personalData["job_title"];
    this.jobSubject = this.personalData["job_subject"];
    this.imagePath = this.personalData["image_path"];
  }

}