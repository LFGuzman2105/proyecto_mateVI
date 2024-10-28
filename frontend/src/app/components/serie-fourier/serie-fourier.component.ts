import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { FourierService } from '../../services/fourier.service';
import { HttpClientModule } from '@angular/common/http';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatRadioModule } from '@angular/material/radio';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatTableModule } from '@angular/material/table';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-serie-fourier',
  standalone: true,
  imports: [FormsModule, HttpClientModule, MatToolbarModule, MatRadioModule, MatSidenavModule, MatFormFieldModule, 
            MatInputModule, MatButtonModule, RouterModule, MatTableModule],
  templateUrl: './serie-fourier.component.html',
  styleUrl: './serie-fourier.component.scss',
  providers: [FourierService]
})
export class SerieFourierComponent {
  nFunciones: string;
  f1: string;
  f2: string;
  f3: string;
  r1_a: string;
  r1_b: string;
  r2_a: string;
  r2_b: string;
  r3_a: string;
  r3_b: string;
  imagenGrafica: string | null;
  data: string | any;
  displayedColumns: string[];
  dataSource: any[];
  an: number;
  bn: number;

  constructor(private fourierService: FourierService) {
    this.nFunciones = "1";
    this.f1 = '';
    this.f2 = '';
    this.f3 = '';
    this.r1_a = '';
    this.r1_b = '';
    this.r2_a = '';
    this.r2_b = '';
    this.r3_a = '';
    this.r3_b = '';
    this.imagenGrafica = null;
    this.data = null;
    this.displayedColumns = ['n', "a0", 'an', 'bn']
    this.dataSource = [];
    this.an = 0;
    this.bn = 0;
  }

  mostrar() {
    if (this.nFunciones == "1" && (this.f1 == '' || this.r1_a == '' || this.r1_b == '')) {
      alert('Faltan datos para mostrar la serie de Fourier.');
    }
    else if (this.nFunciones == "2" && (this.f1 == '' || this.f2 == '' || this.r1_a == '' || this.r1_b == '' || this.r2_a == '' || this.r2_b == '')) {
      alert('Faltan datos para mostrar la serie de Fourier.');
    }
    else if (this.nFunciones == "3" && (this.f1 == '' || this.f2 == '' || this.f3 == '' || this.r1_a == '' || this.r1_b == '' || this.r2_a == '' || this.r2_b == '' 
      || this.r3_a == '' || this.r3_b == '')) {
      alert('Faltan datos para mostrar la serie de Fourier.');
    }
    else {
      this.fourierService.enviarDatos({nFunciones: this.nFunciones, f1: this.f1, f2: this.f2, f3: this.f3, r1_a: this.r1_a, r1_b: this.r1_b,
        r2_a: this.r2_a, r2_b: this.r2_b, r3_a: this.r3_a, r3_b: this.r3_b}).subscribe(response => {
        this.imagenGrafica = 'data:image/png;base64,' + response.imagenGrafica;
        this.data = response;

        this.an = this.data.suma_an;
        this.bn = this.data.suma_bn;
        this.dataSource = [];

        for (let i = 0; i < this.data.N; i++) {
          this.dataSource.push({n: i + 1, a0: this.data.a0, an: this.data.an[i], bn: this.data.bn[i]});
        }
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
    this.imagenGrafica = null;
    this.data = null;
    this.dataSource = [];
    this.an = 0;
    this.bn = 0;
  }
}