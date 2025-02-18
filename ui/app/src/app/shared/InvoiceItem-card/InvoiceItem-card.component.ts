import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './InvoiceItem-card.component.html',
  styleUrls: ['./InvoiceItem-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.InvoiceItem-card]': 'true'
  }
})

export class InvoiceItemCardComponent {


}