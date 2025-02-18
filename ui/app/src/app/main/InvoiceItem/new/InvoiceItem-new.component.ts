import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'InvoiceItem-new',
  templateUrl: './InvoiceItem-new.component.html',
  styleUrls: ['./InvoiceItem-new.component.scss']
})
export class InvoiceItemNewComponent {
  @ViewChild("InvoiceItemForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}