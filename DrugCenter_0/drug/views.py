from django.contrib.auth.decorators import login_required
from .forms import BookFormset
from .models import Book
from django.shortcuts import render, get_object_or_404, redirect
from drug.models import Molecule, Interact_med, Prescription
from .forms import PatientForm, PhysicianForm, PrescriptionzForm, PrescriptionForm, NameForm3, PrescriptionItemForm
from .models import Physician, Patient, Product
import pymongo
from datetime import datetime
import  requests

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb['saln']



# def create_book_normal(request):
#     template_name = 'd/dynamic-form.html'
#     heading_message = 'Formset Demo'
#     if request.method == 'GET':
#         formset = BookFormset(request.GET or None)
#     elif request.method == 'POST':
#         formset = BookFormset(request.POST)
#         if formset.is_valid():
#             b = formset.
#             for form in formset:
#                 # extract name from each form and save
#                 name = form.cleaned_data.get('name')
#                 print(name)
#                 # save book instance
#                 if name:
#                     Book(name=name).save()
#             # once all books are saved, redirect to book list view
#             # return redirect('book_list')
#     return render(request, template_name, {
#         'formset': formset,
#         'heading': heading_message,
# })

def create_book_normal(request):
    print(request.POST)
    # for i in request.POST:
    #     m.update({i[30:-1]: [request.POST[i]]})
    # print(request.POST)
    # print(request.POST['dynamic_form[dynamic_form][0][form-0-name]'])
    # print(request.POST['dynamic_form[dynamic_form][1][form-0-name]'])
    # print(request.POST['dynamic_form[dynamic_form][2][form-0-name]'])
    formset = BookFormset(request.POST)
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
    return render(request, 'd/dynamic-form.html', {'formset': formset})
    # return render(request, 'd/Add New Invoice.html', {'formset': formset})





def HomePage(request):
    return render(request, 'Drug/Daroo/base.html')


def search(request):
    noskh = Prescription.objects.filter(borrower_id=request.user)
    return render(request, 'noskh.html', {'noskhe': noskh})


def index(request):
    q = request.GET.get('InsuranceType')

    if q:
        url = ['https://entities.ttac.ir/Api/SystemInfo/InquirePerson?birthdate=Fri+Apr+24+1992&nationalCode=', q]
        sep = ''
        url = sep.join(url)
        req = requests.get(url)
        req = req.json()
        print(req)
        National = Patient.objects.get(pk=1)
        print(National)
    else:
        National = []
        req = []
    initial_data = {
        'PrescriptionType': 3
    }
    # print(request.POST)
    # noskh = PrescriptionzForm(request.POST or None)
    physician = PhysicianForm(request.POST or None)
    patient = PatientForm(request.POST or None)
    # noskh3 = NameForm3(request.POST or None)
    prescription = PrescriptionForm(request.POST or None, initial=initial_data)
    prescriptionItem = PrescriptionItemForm(request.POST or None)
    Itemlist = []

    if prescription.is_valid() and prescriptionItem.is_valid():
        sep = prescription.clean()
        sep3 = prescriptionItem.clean()
        Itemlist.append(sep3)
        # print(Itemlist)
        # print(sep)

        if physician.is_valid():
            sep0 = physician.clean()
            # print(sep0)
            phys = Physician.objects.filter(MedicalCode=sep0['MedicalCode'])
            for i in phys:
                fc = i
            if not phys:
                fc = physician.save()

            if patient.is_valid():
                sep1 = patient.clean()
                # print(sep1)
                pat = Patient.objects.filter(NationalCode=sep1['NationalCode'])
                if not pat:
                    patient.save()

                invoice = mycol.find_one({'Serial': sep['Serial'], 'Page': sep['Page']})
                # print(invoice)
                if invoice:
                    print('rep')
                else:
                    mycol.insert_one(
                        {
                            'user': request.user.id,
                            'NationalCode': sep1['NationalCode'],
                            'MedicalCode': sep0['MedicalCode'],
                            'PrescriptionDate': datetime.combine(sep['PrescriptionDate'], datetime.min.time()),
                            'ValidityDate': datetime.combine(sep['ValidityDate'], datetime.min.time()),
                            'DeliveryDate': datetime.combine(sep['DeliveryDate'], datetime.min.time()),
                            'Serial': sep['Serial'],
                            'Page': sep['Page'],
                            'PrescriptionType': sep['PrescriptionType'],
                            'InsuranceType': sep['InsuranceType'],
                            'Items': Itemlist
                        }
                    )

    #
    # if noskh.is_valid():
    #     fs = noskh.save()
    #     fs.physician = fc
    #     fs.patient = fz
    #     fs.user = request.user
    #     fs.save()
    #
    # if noskh3.is_valid():
    #     sep2 = noskh3.clean()
    #     fq = noskh3.save()
    #     fq.product = Product.objects.get(id=sep2['tari'])
    #     fq.prescription = fs
    #     fq.save()

    return render(request, 'Drug/Daroo/factor.html',
                  {'prescription': prescription, 'physician': physician, 'patient': patient,
                   'prescriptionItem': prescriptionItem, 'National': National, 'req': req})


# def get_name(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})

# from drug.search_indexes import Interact_medIndex
# from .forms import NotesSearchForm
# from haystack.query import SearchQuerySet
# from django.shortcuts import render_to_response


# def search_title(request):
#     interact = Interact_med.objects.filter(object__icontains='m')
#     return render('search/indexes/search.html', {'interact': interact})


# def notes(request):
#     form = NotesSearchForm(request.GET)
#     notes = form.search()
#     return render(request, 'search/search.html', {'notes': notes})


# class ProductView(TemplateView):
#     def get(self, request, product_id):
#         product = get_object_or_404(Product)
#         # dru = print(product.drug_id)
#         # drug = get_object_or_404(Drug.objects.filter(id=dru))
#         # return render(request, 'product.html', {'product': product})
#         return render(request, 'product.html', {'product': product})


def Home(request):
    q = request.GET.get('q')

    if q:
        mol = Molecule.objects.filter(id=q)

        if mol:
            for i in mol:
                m = i.MoleculeName.capitalize()
                interact_0 = Interact_med.objects.filter(object__icontains=m)
                interact_1 = Interact_med.objects.filter(subject__icontains=m)
                interact = (interact_0 | interact_1).distinct()
        else:
            mol = ''
            interact = ''
    else:
        mol = ''
        interact = ''

    return render(request, 'Drug/search/SearchResult.html', {'mol': mol, 'interact': interact})
