import { Component, OnInit } from '@angular/core';
import { HardDataService } from '../../services/hard-data.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  hardData: any;
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
    this.navBarItems = this.hardData["navbar_items"];
  }

}
