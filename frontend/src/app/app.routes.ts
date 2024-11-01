import { Routes } from '@angular/router';
import { SerieFourierComponent } from './components/serie-fourier/serie-fourier.component';
import { HomeComponent } from './components/home/home.component';
import { ToolbarComponent } from './components/toolbar/toolbar.component';
import { FftFourierComponent } from './components/fft-fourier/fft-fourier.component';

export const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'serie_fourier', component: SerieFourierComponent },
    { path: 'fft', component: FftFourierComponent },
    { path: 'toolbar', component: ToolbarComponent },
    { path: '', redirectTo: '/home', pathMatch: 'full'},
    { path: '**', redirectTo: '/home'}
];
