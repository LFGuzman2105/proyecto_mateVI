import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SerieFourierComponent } from './components/serie-fourier/serie-fourier.component';
import { HomeComponent } from './components/home/home.component';
import { ToolbarComponent } from './components/toolbar/toolbar.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, SerieFourierComponent, HomeComponent, ToolbarComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'frontend';
}
