from django.http import HttpResponse
from datetime import datetime
from .models import Project, System, Instrument, Valve, Pump, Pipe, Tank, Equipment
from data.models import Fluid, Material, PipeSize
from django.shortcuts import get_object_or_404, render
import io
from xlsxwriter.workbook import Workbook

def valve_rfq_xlsx_view(request, project_slug):

    project = get_object_or_404(Project, slug=project_slug).__dict__['name']
    valves_queryset = Valve.objects.filter(project__slug=project_slug, procurement_status='rq').exclude(vendor__isnull=True).order_by('vendor')
    valves = [i.__dict__ for i in list(valves_queryset)]
    print(valves[0])
    modified_date = "{:%B %d, %Y  %H:%M}".format(Valve.history.all().order_by('-history_date')[0].history_date)
    output = io.BytesIO()

    workbook = Workbook(output, {'in_memory': True})
    
    # worksheet = workbook.add_worksheet()

    # row = 0
    # col = 0

    # worksheet.write(row, col, 'Hello, world!')
    # row += 1
    
    # for i, valve in enumerate(valves):
    #     worksheet.write(row, col, valve['name'])
    #     row += 1

    header = 'Consolidated Water Engineering'
    doc_name = 'Valve Specification Sheet'
    creation_date = '2017/10/19 8:32am'

    worksheet = workbook.add_worksheet('Valve RFQ')

    # Create all of the types of cell formats
    bold = workbook.add_format({'bold': 1})
    head1 = workbook.add_format({'font_size': 16})
    head2 = workbook.add_format({'font_size': 14})
    head3 = workbook.add_format({'font_size': 12})
    head1_bold = workbook.add_format({'font_size': 16, 'bold': 1})
    head2_bold = workbook.add_format({'font_size': 14, 'bold': 1})
    head3_bold = workbook.add_format({'font_size': 12, 'bold': 1})
    bold_centered = workbook.add_format(
        {
            'bold': 1,
            'align': 'center',
            'valign':'vcenter',
            'text_wrap': 1,
            'border': 1,
            'locked': 1,
        })
    table_value = workbook.add_format(
        {
            'align': 'center',
            'valign':'vcenter',
            'text_wrap': 1,
            'border': 1,
            'locked': 1,
        })
    table_value_input = workbook.add_format(
        {
            'align': 'center',
            'valign':'vcenter',
            'text_wrap': 1,
            'border': 1,
            'bg_color': '#ccffff',
        })
    header_value_input = workbook.add_format(
        {
            'align': 'center',
            'valign':'vcenter',
            'text_wrap': 1,
            'bg_color': '#ccffff',
        })
    date_format = workbook.add_format({'num_format': 'mmmm d, yyyy  hh:mm', 'locked': 1})
    now = datetime.now()
    # Write some page headers.
    worksheet.write('A1', header, head1_bold)
    worksheet.write('A2', doc_name, head2)
    worksheet.write('A3', project, head3)
    worksheet.write('A4', 'Document Number:', bold)
    worksheet.write('D4', None, header_value_input)
    worksheet.write('A5', 'Creation Date:', bold)
    worksheet.write_datetime('D5', now, date_format)
    worksheet.write('A6', 'Last Valve Modified:', bold)
    worksheet.write('D6', modified_date)


    # Set column widths
    worksheet.set_column(0,0, 7)
    worksheet.set_column(1,1, 7)
    worksheet.set_column(2,2, 17)
    worksheet.set_column(3,3, 14)
    worksheet.set_column(4,4, 14)
    worksheet.set_column(5,5, 14)
    worksheet.set_column(6,6, 14)
    worksheet.set_column(7,7, 14)
    worksheet.set_column(8,8, 14)
    worksheet.set_column(9,9, 14)
    worksheet.set_column(10,10, 14)
    worksheet.set_column(11,11, 14)
    worksheet.set_column(12,12, 14)
    worksheet.set_column(13,13, 30)
    worksheet.set_column(15,15, 9)
    worksheet.set_column(15,15, 9)
    worksheet.set_column(14,14, 9)
    worksheet.set_column(16,16, 9)
    worksheet.set_column(16,16, 9)

    # Write some data headers
    worksheet.write(9,0, 'Line', bold_centered)
    worksheet.write(9,1, 'P&ID Tag', bold_centered)
    worksheet.write(9,2, 'Description', bold_centered)
    worksheet.write(9,3, 'Quantity', bold_centered)
    worksheet.write(9,4, 'Manufacturer', bold_centered)
    worksheet.write(9,5, 'Part Number', bold_centered)
    worksheet.write(9,6, 'Nominal Size', bold_centered)
    worksheet.write(9,7, 'Materials', bold_centered)
    worksheet.write(9,8, 'End Connections', bold_centered)
    worksheet.write(9,9, 'Flange Class', bold_centered)
    worksheet.write(9,10, 'Max. Temp.', bold_centered)
    worksheet.write(9,11, 'Max. Pressure', bold_centered)
    worksheet.write(9,12, 'Equivalent Acceptable', bold_centered)
    worksheet.write(9,13, 'Detailed Description', bold_centered)
    worksheet.write(9,14, 'Unit Cost', bold_centered)
    worksheet.write(9,16, 'Unit Cost', bold_centered)
    worksheet.write(9,18, 'Unit Cost', bold_centered)
    worksheet.write(9,15, 'Total Cost', bold_centered)
    worksheet.write(9,17, 'Total Cost', bold_centered)
    worksheet.write(9,19, 'Total Cost', bold_centered)
    worksheet.merge_range("O9:P9", 'Vendor A', bold_centered)
    worksheet.merge_range("Q9:R9", 'Vendor B', bold_centered)
    worksheet.merge_range("S9:T9", 'Vendor C', bold_centered)

    row = 10
    for i, valve in enumerate(valves):
        worksheet.write(row + i, 0, i + 1, table_value)
        worksheet.write(row + i,1, valve['full_pid_tag_number'], table_value)
        worksheet.write(row + i,2, valve['name'], table_value)
        worksheet.write(row + i,3, None, table_value_input)
        worksheet.write(row + i,4, valve['vendor'], table_value)
        worksheet.write(row + i,5, valve['valve_model'], table_value)
        if valve['connection_size_id']:
            connection_size = get_object_or_404(PipeSize, pk=valve['connection_size_id']).append_units()
        else:
            connection_size = None
        worksheet.write(row + i,6, connection_size, table_value)
        if valve['material_id']:
            material = get_object_or_404(Material, pk=valve['material_id']).__dict__['name']
        else:
            material = None
        worksheet.write(row + i,7, material, table_value)
        worksheet.write(row + i,8, valve['connection_type'], table_value)
        worksheet.write(row + i,9, valve['pipe_flange_class'], table_value)
        worksheet.write(row + i,10, valve['temperature'], table_value)
        worksheet.write(row + i,11, valve['pressure'], table_value)
        worksheet.write(row + i,12, None, table_value_input)
        worksheet.write(row + i,13, valve['detailed_description'], table_value)
        worksheet.write(row + i,14, None, table_value_input)
        worksheet.write(row + i,16, None, table_value_input)
        worksheet.write(row + i,18, None, table_value_input)
        worksheet.write(row + i,15, 'Total Cost', table_value)
        worksheet.write(row + i,17, 'Total Cost', table_value)
        worksheet.write(row + i,19, 'Total Cost', table_value)

    workbook.close()
    output.seek(0)
    filename = 'attachment; filename=Valve Spec Sheet ' + now.strftime("%b-%d-%Y-%H%M%S") + '.xlsx'
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = filename

    return response