import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FourierService {

  constructor(private http: HttpClient) { }

  private baseUrl: string = 'http://localhost:5000';

  enviarDatos(response: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/serie_fourier`, response);
  }
}