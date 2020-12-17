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

  constructor(private authService: AuthService, private route: Router) { }

  ngOnInit(): void {
  }

  onLogin(value) {
    this.authService.login(value).subscribe(
       data => {
        localStorage.setItem('isLoggedIn', 'true');
        localStorage.setItem('token', data.token);
        this.route.navigateByUrl('/list');
      },
      error => {
        this.errorMessage = error.error.message;
        this.isSignUpFailed = true;
      }
    );
  }
}
