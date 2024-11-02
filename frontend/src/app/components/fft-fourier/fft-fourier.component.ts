import { Component, signal } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatFormField, MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { FourierService } from '../../services/fourier.service';
import { HttpClientModule } from '@angular/common/http';
import { Console } from 'console';
import { MatOption, MatSelect } from '@angular/material/select';

interface Images {
  value: string;
  name: string;
}

@Component({
  selector: 'app-fft-fourier',
  standalone: true,
  imports: [
    MatFormFieldModule, 
    MatInputModule, 
    FormsModule, 
    ReactiveFormsModule,
    MatButtonModule, 
    HttpClientModule,
    MatSelect,
    MatOption,
    MatFormField,
  ],
  templateUrl: './fft-fourier.component.html',
  styleUrl: './fft-fourier.component.scss'
})
export class FftFourierComponent {
  selectedimg: string = '';
  filtered_images: string = '';
  images: Images[] = [
    {value: '1', name: 'Imagen 1'},
    {value: '2', name: 'Imagen 2'},
    {value: '3', name: 'Imagen 3'},
    {value: '4', name: 'Imagen 4'},
    {value: '5', name: 'Imagen Personalizada'},
  ];

  constructor(
    private fourierService: FourierService
  ) { }

  reset() {
    this.filtered_images = '';
  }

  onSubmit(): void {
    this.filtered_images = '';
    if (!this.selectedimg) {
      alert('No ha seleccionado ninguna imagen.') ;
      console.log(this.selectedimg);
      return;
    }

    const formData = {
      img: this.selectedimg,
    }

    this.fourierService.sendFftData(formData).subscribe(response => {
      this.filtered_images = 'data:image/png;base64,' + response.imagen_filtrada;
    });
  }
}
