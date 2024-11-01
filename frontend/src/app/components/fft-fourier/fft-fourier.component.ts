import { Component, signal } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatFormField, MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'app-fft-fourier',
  standalone: true,
  imports: [
    MatFormFieldModule, 
    MatInputModule, 
    FormsModule, 
    ReactiveFormsModule,
    MatButtonModule, 
  ],
  templateUrl: './fft-fourier.component.html',
  styleUrl: './fft-fourier.component.scss'
})
export class FftFourierComponent {
  imageForm: FormGroup = new FormGroup('');
  selectedFile: File | null = null;

  constructor(
    private dataImage: FormBuilder
  ) {
    this.imageForm = this.dataImage.group({})
  }

  onFileSelect(event: Event): void {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files.length > 0) {
      this.selectedFile = target.files[0];
    }
  }

  onSubmit(): void {
    if (!this.selectedFile) {
      console.error("No file selected");
      return;
    }

    console.log(this.selectedFile);
  }
}
