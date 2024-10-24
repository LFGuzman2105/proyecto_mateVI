import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { FourierService } from '../../services/fourier.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-serie-fourier',
  standalone: true,
  imports: [FormsModule, HttpClientModule],
  templateUrl: './serie-fourier.component.html',
  styleUrl: './serie-fourier.component.scss',
  providers: [FourierService]
})
export class SerieFourierComponent {
  nFunciones: number;
  f1: string;
  f2: string;
  f3: string;
  r1_a: string;
  r1_b: string;
  r2_a: string;
  r2_b: string;
  r3_a: string;
  r3_b: string;

  constructor(private fourierService: FourierService) {
    this.nFunciones = 1;
    this.f1 = '';
    this.f2 = '';
    this.f3 = '';
    this.r1_a = '';
    this.r1_b = '';
    this.r2_a = '';
    this.r2_b = '';
    this.r3_a = '';
    this.r3_b = '';
  }

  mostrar() {
    if (this.nFunciones == 1 && (this.f1 == '' || this.r1_a == '' || this.r1_b == '')) {
      alert('Faltan datos para mostrar la serie de Fourier.');
    }
    else if (this.nFunciones == 2 && (this.f1 == '' || this.f2 == '' || this.r1_a == '' || this.r1_b == '' || this.r2_a == '' || this.r2_b == '')) {
      alert('Faltan datos para mostrar la serie de Fourier.');
    }
    else if (this.nFunciones == 3 && (this.f1 == '' || this.f2 == '' || this.f3 == '' || this.r1_a == '' || this.r1_b == '' || this.r2_a == '' || this.r2_b == '' 
      || this.r3_a == '' || this.r3_b == '')) {
      alert('Faltan datos para mostrar la serie de Fourier.');
    }
    else {
      this.fourierService.enviarDatos({nFunciones: this.nFunciones, f1: this.f1, f2: this.f2, f3: this.f3, r1_a: this.r1_a, r1_b: this.r1_b,
        r2_a: this.r2_a, r2_b: this.r2_b, r3_a: this.r3_a, r3_b: this.r3_b}).subscribe(data => {
        console.log('Respuesta después de enviar datos:', data);
      });
    }
  }

  limpiar() {
    this.f1 = '';
    this.f2 = '';
    this.f3 = '';
    this.r1_a = '';
    this.r1_b = '';
    this.r2_a = '';
    this.r2_b = '';
    this.r3_a = '';
    this.r3_b = '';
  }
}