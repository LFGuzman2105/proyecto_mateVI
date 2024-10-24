import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SerieFourierComponent } from './components/serie-fourier/serie-fourier.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, SerieFourierComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'frontend';
}
