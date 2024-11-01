import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FftFourierComponent } from './fft-fourier.component';

describe('FftFourierComponent', () => {
  let component: FftFourierComponent;
  let fixture: ComponentFixture<FftFourierComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FftFourierComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FftFourierComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
