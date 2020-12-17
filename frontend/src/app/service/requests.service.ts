import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RequestsService {

  constructor(private httpClient: HttpClient) { }

  getEspecialidades(token): Observable<any> {
    return this.httpClient.get('http://localhost:8000/especialidades/', {
      headers: new HttpHeaders({
        Authorization: 'JWT ' + token
      })
    });
  }

  getMedicos(token: string, especialidadeId: number): Observable<any> {
    return this.httpClient.get('http://localhost:8000/medicos/?especialidade=' + especialidadeId, {
      headers: new HttpHeaders({
        Authorization: 'JWT ' + token
      })
    });
  }

  getAgenda(token: string, medicoId: number): Observable<any> {
    return this.httpClient.get('http://localhost:8000/agendas/?medico=' + medicoId, {
      headers: new HttpHeaders({
        Authorization: 'JWT ' + token
      })
    });
  }

  getAgendaByDay(token: string, dia: string): Observable<any> {
    return this.httpClient.get('http://localhost:8000/agendas/?dia=' + dia, {
      headers: new HttpHeaders({
        Authorization: 'JWT ' + token
      })
    });
  }

  makeConsulta(token: string, horarioValue: string, agendaIdValue): Observable<any> {
    return this.httpClient.post('http://localhost:8000/consultas/', {
      horario: horarioValue,
      agenda_id: agendaIdValue
    }, {
      headers: new HttpHeaders({
        Authorization: 'JWT ' + token
      })
    });
  }

  getConsultas(token: string): Observable<any> {
    return this.httpClient.get('http://localhost:8000/consultas', {
      headers: new HttpHeaders({
        Authorization: 'JWT ' + token
      })
    });
  }

  deleteConsultas(token: string, consultaId: number): Observable<any> {
    return this.httpClient.delete('http://localhost:8000/consultas/' + consultaId.toString() + '/', {
      headers: new HttpHeaders({
        Authorization: 'JWT ' + token
      })
    });
  }
}
