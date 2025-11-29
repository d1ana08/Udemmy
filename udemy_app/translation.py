from .models import Category, SubCategory, Course, Lesson,Assignment, Option, Question, Exam, Review
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(SubCategory)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Course)
class ProductTranslationOptions(TranslationOptions):
    fields = ('subcategory', 'course_name', 'description')


@register(Lesson)
class ProductTranslationOptions(TranslationOptions):
    fields = ('tittle', 'content')


@register(Assignment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('tittle', 'description')


@register(Option)
class ProductTranslationOptions(TranslationOptions):
    fields = ('option_name',)


@register(Question)
class ProductTranslationOptions(TranslationOptions):
    fields = ('questions_name', 'questions_text')


@register(Exam)
class ProductTranslationOptions(TranslationOptions):
    fields = ('tittle',)


@register(Review)
class ProductTranslationOptions(TranslationOptions):
    fields = ('comment',)