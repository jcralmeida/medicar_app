import { Component, OnInit } from '@angular/core';
import { AuthService } from '../service/auth.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  constructor(private router: Router, private authService: AuthService) { }

  showSpinner = false;

  ngOnInit(): void {
  }

  onRegister(form) {
    this.authService.register(form).subscribe(() => {
      this.showSpinner = true;
      setTimeout(() => {
        this.showSpinner = false;
          this.router.navigateByUrl('/login');
      }, 1000);
    });
  }
}
