import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SerieFourierComponent } from './components/serie-fourier/serie-fourier.component';
import { HomeComponent } from './components/home/home.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, SerieFourierComponent, HomeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'frontend';
}
