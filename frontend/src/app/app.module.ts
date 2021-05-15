import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { CoursesComponent } from './components/courses/courses.component';
import { CvComponent } from './components/cv/cv/cv.component';
import { EducationComponent } from './components/cv/education/education.component';
import { ExperiencesComponent } from './components/cv/experiences/experiences.component';
import { HeaderImageComponent } from './components/header-image/header-image.component';
import { PhysicsComponent } from './components/physics/physics.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    DashboardComponent,
    CoursesComponent,
    CvComponent,
    EducationComponent,
    ExperiencesComponent,
    HeaderImageComponent,
    PhysicsComponent,
    SidebarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
