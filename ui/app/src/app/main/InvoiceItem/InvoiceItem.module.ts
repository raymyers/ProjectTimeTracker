import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {INVOICEITEM_MODULE_DECLARATIONS, InvoiceItemRoutingModule} from  './InvoiceItem-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    InvoiceItemRoutingModule
  ],
  declarations: INVOICEITEM_MODULE_DECLARATIONS,
  exports: INVOICEITEM_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class InvoiceItemModule { }