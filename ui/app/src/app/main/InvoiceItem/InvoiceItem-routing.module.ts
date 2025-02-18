import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InvoiceItemHomeComponent } from './home/InvoiceItem-home.component';
import { InvoiceItemNewComponent } from './new/InvoiceItem-new.component';
import { InvoiceItemDetailComponent } from './detail/InvoiceItem-detail.component';

const routes: Routes = [
  {path: '', component: InvoiceItemHomeComponent},
  { path: 'new', component: InvoiceItemNewComponent },
  { path: ':id', component: InvoiceItemDetailComponent,
    data: {
      oPermission: {
        permissionId: 'InvoiceItem-detail-permissions'
      }
    }
  }
];

export const INVOICEITEM_MODULE_DECLARATIONS = [
    InvoiceItemHomeComponent,
    InvoiceItemNewComponent,
    InvoiceItemDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class InvoiceItemRoutingModule { }