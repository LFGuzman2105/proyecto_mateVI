import { Component } from '@angular/core';
import { MatToolbar } from '@angular/material/toolbar';
import { RouterModule } from '@angular/router';
import {MatTabsModule} from '@angular/material/tabs';
import { SerieFourierComponent } from '../serie-fourier/serie-fourier.component';
import { FftFourierComponent } from '../fft-fourier/fft-fourier.component';

@Component({
  selector: 'app-toolbar',
  standalone: true,
  imports: [
    RouterModule, 
    MatToolbar, 
    MatTabsModule, 
    SerieFourierComponent,
    FftFourierComponent
  ],
  templateUrl: './toolbar.component.html',
  styleUrl: './toolbar.component.scss'
})
export class ToolbarComponent {

}
