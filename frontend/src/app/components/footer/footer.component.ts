import { Component, OnInit } from '@angular/core';
import { HardDataService } from '../../services/hard-data.service';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {
  hardData: any;
  personalData: any;
  facebook:string = "";
  instagram: string = "";
  linkedin: string = "";
  github: string = "";
  medium: string = "";
  youtube: string = "";
  twitter: string = "";
  telegram: string = "";
  soundcloud: string = "";
  slideshare: string = "";
  skype: string = "";
  inspire: string = "";
  googleScholar: string = "";
  researchgate: string = "";
  goodreads: string = "";
  anaconda: string = "";
  stackoverflow: string = "";

  
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
    this.facebook = this.personalData.facebook;
    this.instagram = this.personalData.instagram;
    this.linkedin = this.personalData.linkedin;
    this.github = this.personalData.github;
    this.medium = this.personalData.medium;
    this.youtube = this.personalData.youtube;
    this.twitter = this.personalData.twitter;
    this.telegram = this.personalData.telegram;
    this.soundcloud = this.personalData.soundcloud;
    this.slideshare = this.personalData.slideshare;
    this.skype = this.personalData.skype;
    this.inspire = this.personalData.inspire;
    this.googleScholar = this.personalData.google_scholar;
    this.researchgate = this.personalData.researchgate;
    this.goodreads = this.personalData.goodreads;
    this.anaconda = this.personalData.anaconda;
    this.stackoverflow = this.personalData.stackoverflow;
  }

}
