import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private httpClient: HttpClient) { }

  login(credentials): Observable<any> {
    return this.httpClient.post('http://localhost:8000/login/', {
      username: credentials.username,
      password: credentials.password
    })
  }

  register(user): Observable<any> {
    return this.httpClient.post('http://localhost:8000/registration/', {
      username: user.username,
      email: user.email,
      password: user.password1,
      repeatedPassword: user.password2
    })
  }
}
