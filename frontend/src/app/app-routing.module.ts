import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CoursesComponent } from './components/courses/courses.component';
import { CvComponent } from './components/cv/cv/cv.component';
import { EducationComponent } from './components/cv/education/education.component';
import { DashboardComponent } from './components/dashboard/dashboard.component'
import { PhysicsComponent } from './components/physics/physics.component';

const routes: Routes = [
  { path: 'dashboard', component: DashboardComponent },
  { path: "courses", component: CoursesComponent },
  { path: "cv", component: CvComponent },
  { path: "home", component: DashboardComponent},
  { path: "education", component: EducationComponent},
  { path: "physics", component: PhysicsComponent},
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
