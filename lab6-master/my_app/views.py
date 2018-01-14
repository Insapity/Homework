from datetime import datetime
from .models import *
from my_app.registration import *
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import View, ListView
from my_app.forms import RegistrForm
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def main(request):
    return render(request, 'main.html', locals())

def tickets(request):
    return render(request, 'tickets.html')

def hello(request):
    return render(request, 'hello.html')

def new(request):
    return render(request, 'new.html')


def db(request):
    return render(request, 'db.html', locals())


class HotelView(ListView):
    model = Hotel
    template_name = 'hotelsbd.html'


class HumanView(ListView):
    model = Human
    template_name = 'countrybd.html'


class UserssView(ListView):
    model = Registr
    template_name = 'usersbd.html'


class NomeraView(ListView):
    model = Nomer
    template_name = 'nomerabd.html'


class RegistrsList(ListView):
    form_class = RegistrForm
    model = Registr
    template_name = "tickets.html"
    paginate_by = 2
    nomera = Nomer.objects.all()
    human = Human.objects.all()
    context = {"form": form_class, "nomera": nomera, "human": human}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nomera'] = Nomer.objects.all()
        return context


    def post(self, request):
        form = self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('course_url', args=(instance.pk,)))
        return render(request, self.template_name, {'form': form})


def course_add(request):
    nomera = Nomer.objects.all()
    human = Human.objects.all()
    form = RegistrForm(request.POST or None, request.FILES or None)
    context = {"form": form, "nomera": nomera, "human": human}
    print(form.errors)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('course_url', args=(instance.pk, )))
    return render(request, "ticket_element.html", context)


def hotels(request, id):
    name = ['Park_info', 'Alexandria_info', 'Voshod_info']
    Park_info = 'The Park Hotel situated in the heart of Sliema just walking distance from the Shopping Mecca and only 2 km from the UNESCO world heritage city Valletta, offers a unique location. Warmth, Style & Service are what defines Park Hotel an environment to enjoy and indulge. Bedroomed Hotel which boasts a wide selection of Room Categories, maintained to a comfortable standard set with amenities to make every stay at Park Hotel a memorable one. Our Roof Top Swimming Pool Terrace offers a relaxing area with amazing views of The Grand Harbour. Complimentary Wi-Fi is also available in Hotel Lobby & Bar area. Our hotel is the perfect option for experiencing the Maltese Islands being within easy access to Malta’s most popular Historical sites. We look forward to extending our warmest welcome to you.'
    Alexandria_info =  'До пляжа можно дойти всего за 3 минуты. Отель "Александрия" находится в 5 минутах ходьбы от берега Черного моря и располагает сауной, крытым и открытым бассейнами. К услугам гостей апартаменты с кондиционером и телевизором с плоским экраном. Все апартаменты отеля "Александрия" оформлены в красных и коричневых тонах и оснащены шкафом и кухней. В ванных комнатах установлен душ. В элегантном ресторане отеля "Александрия" подают блюда европейской и национальной украинской кухни. Для отдыха в отеле "Александрия" есть сауна и спа-салон с массажным кабинетом. Также к услугам гостей бильярд, кинотеатр, ночной клуб и конференц-зал.'
    Voshod_info = 'Отель Voshod расположен на набережной Слимы, в 3 минутах ходьбы от скалистого пляжа. Все номера оборудованы телевизором, холодильником и принадлежностями для чая/кофе. Летом на террасе подают завтрак.'
    info = [Park_info, Alexandria_info, Voshod_info]
    data1 = {'hotel': {'id': id}}
    data2 = {'hotels': [{'id': '1', 'hotel_name': 'Park Hotel', 'info': Park_info},
                       {'id': '2', 'hotel_name': 'Alexandria', 'info': Alexandria_info},
                       {'id': '3', 'hotel_name': 'Voshod', 'info': Voshod_info}]}
    return render(request, 'hotels.html', locals())


class hotelsview(View):
    def get(self, request):
        nomera = Nomer.objects.all()
        human = Human.objects.all()
        form = RegistrForm(request.POST or None, request.FILES or None)
        context = {"form": form, "nomera": nomera, "human": human}
        print(form.errors)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('course_url', args=(instance.pk,)))
        return render(request, "ticket.html", context)


class hotelview(View):
    def get(self, request, id):
        nomera = Nomer.objects.all()
        human = Human.objects.all()
        form = RegistrForm(request.POST or None, request.FILES or None)
        context = {"form": form, "nomera": nomera, "human": human}
        print(form.errors)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('course_url', args=(instance.pk,)))
        return render(request, "ticket_element.html", context)


def registration(request):
    errors = {'username': '', 'password': '', 'password2': '', 'email': '', 'firstname': '', 'surname': ''}
    error_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
            error_flag = True
        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'
            error_flag = True
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
            error_flag = True
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
            error_flag = True
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
            error_flag = True
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not error_flag:
            # ...
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=surname)
            return HttpResponseRedirect('/login/')
    return render(request, 'registration.html', locals())


def login(request):
    error = ""
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/success/')
        else:
            error = "Пользователь не найден"
    return render(request, 'login.html', locals())


@login_required()
def success(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/login/')
    return render(request, 'success.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')


def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('firstname'),
                                            last_name=request.POST.get('surname'))
            # ...
            return HttpResponseRedirect('/login/')
        else:
            form = RegistrationForm()
    return render(request, 'registration2.html', {'form': form})

def related_json_nomers(request, hotel_name):
    current_hotel = Nomer.objects.get(hotell=hotel_name)
    hotell = Hotel.objects.all().filter(hotel_name=current_hotel)
    json_nomers = serializers.serialize("json", hotell)
    return HttpResponse(json_nomers, content_type="application/javascript")


def all_json_registrs(request):
    registr = Registr.objects.all()
    json_hotels = serializers.serialize("json", registr, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(json_hotels, content_type="application/javascript")


def registr(request, course_id):
    reg_info = Registr.objects.all().filter(id_registr=course_id)
    Registr.objects.get(id_registr=course_id)
    paginate_by = 2
    if request.method == 'POST':
        Registr.objects.get(id_registr=course_id)
    model = Registr
    return render(request, "ticket.html", {'course': Registr.objects.get(id_registr=course_id)},  locals())


