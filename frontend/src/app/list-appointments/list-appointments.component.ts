import { Component, OnInit } from '@angular/core';
import { AuthService } from '../service/auth.service';
import { Router } from '@angular/router';
import {ModalDismissReasons, NgbModal} from '@ng-bootstrap/ng-bootstrap';
import {RequestsService} from '../service/requests.service';

@Component({
  selector: 'app-list-appointments',
  templateUrl: './list-appointments.component.html',
  styleUrls: ['./list-appointments.component.css']
})
export class ListAppointmentsComponent implements OnInit {

   token: string;
   closeResult: string;
   especialidadeList: any = [];
   medicosList: any = [];
   agendaList: any = [];
   horarioList: any = [];
   agendaId: number;
   horarioEscolhido: string;
   consultaList: any = [];

  constructor(
    private modalService: NgbModal,
    private router: Router,
    private authService: AuthService,
    private requestsService: RequestsService
  ) { }

  ngOnInit(): void {
    this.token = localStorage.getItem('token');
    this.retrieveEspecialidade();
    this.retrieveConsultas();
  }

  logout(): void {
    this.authService.logout();
    this.router.navigateByUrl('/login');
  }

  open(content) {
    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'}).result.then((result) => {
      this.closeResult = `Closed with: ${result}`;
    }, (reason) => {
      this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
    });
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return `with: ${reason}`;
    }
  }

  especialidadeChangeEvent(event): void {
    this.retrieveMedicos(event.target.value);
  }

  medicoChangeEvent(event): void {
    this.retrieveAgenda(event.target.value);
  }

  diaChangeEvent(event): void {
    this.retrieveAgendaByDay(event.target.value);
  }

  horarioChangeEvent(event): void {
    this.horarioEscolhido = event.target.value;
  }

  retrieveEspecialidade(): void{
    this.requestsService.getEspecialidades(this.token).subscribe(
      responseData => {
        this.especialidadeList = responseData;
      }
    );
  }

  retrieveMedicos(especialidadeId): void {
    this.requestsService.getMedicos(this.token, especialidadeId).subscribe(
      responseData => {
        this.medicosList = responseData;
      }
    );
  }

  retrieveAgenda(medicoId): void {
    this.requestsService.getAgenda(this.token, medicoId).subscribe(
      responseData => {
        this.agendaList = responseData;
      }
    );
  }

  retrieveAgendaByDay(dia): void {
    this.requestsService.getAgendaByDay(this.token, dia).subscribe(
      responseData => {
        this.horarioList = responseData[0].horario;
        this.agendaId = responseData[0].id;
      }
    );
  }

  createConsulta(): void {
    this.requestsService.makeConsulta(
      this.token, this.horarioEscolhido, this.agendaId).subscribe();
  }

  retrieveConsultas(): void {
    this.requestsService.getConsultas(this.token).subscribe(
      responseData => {
        this.consultaList = responseData;
      }
    );
  }

  deleteConsulta(consultaId: number): void {
    console.log(consultaId);
    this.requestsService.deleteConsultas(this.token, consultaId).subscribe();
  }
}
