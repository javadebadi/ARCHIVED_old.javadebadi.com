import { Component, OnInit } from '@angular/core';
import { HardDataService } from '../../services/hard-data.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.sass']
})
export class HeaderComponent implements OnInit {
  hardData: any;
  personalData: any;
  fullName: string = "";
  jobTitle: string = "";
  jobSubject: string = "";
  imagePath: string = "";
  navBarItems: any[] = [];

  constructor(
    private hardDataService: HardDataService
  ) {}
  
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
    this.navBarItems = this.hardData["navbar_items"];
  }

}
