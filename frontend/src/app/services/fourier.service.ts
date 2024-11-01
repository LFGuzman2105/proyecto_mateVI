import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FourierService {
  private headers = new HttpHeaders({
    'Content-Type': 'application/json' // Puedes ajustar el tipo de contenido según sea necesario
  });
  private baseUrl: string = 'http://localhost:5000';

  constructor(private http: HttpClient) { }


  enviarDatos(response: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/serie_fourier`, response);
  }

  sendFftData(response: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/fft`, response, { headers: this.headers });
  }
}