import { Routes } from '@angular/router';
import { SerieFourierComponent } from './components/serie-fourier/serie-fourier.component';
import { HomeComponent } from './components/home/home.component';

export const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'serie_fourier', component: SerieFourierComponent },
    { path: '', redirectTo: '/home', pathMatch: 'full'},
    { path: '**', redirectTo: '/home'}
];
