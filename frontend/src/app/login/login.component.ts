import { Component, OnInit } from '@angular/core';
import { AuthService } from '../service/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  isSignUpFailed = false;
  errorMessage = '';

  showSpinner: boolean = false;

  constructor(
    private authService: AuthService,
    private route: Router,

    ) { }

  ngOnInit(): void {
  }

  onLogin(value) {
    this.authService.login(value).subscribe(
       data => {
        this.showSpinner = true;
        setTimeout(() => {
          localStorage.setItem('isLoggedIn', 'true');
          localStorage.setItem('token', data.token);
          this.showSpinner = false;
          this.route.navigateByUrl('/list');
        }, 1000);
      },
      error => {
        this.errorMessage = error.error.message;
        this.isSignUpFailed = true;
      }
    );
  }
}
