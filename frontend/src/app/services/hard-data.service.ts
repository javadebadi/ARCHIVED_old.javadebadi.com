import { Injectable } from '@angular/core';
import { HARDDATA } from '../data';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HardDataService {

  constructor() { }

  getHardData() {
    const hardData = of(HARDDATA);
    return hardData;
  }

}
