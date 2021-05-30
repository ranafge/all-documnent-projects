from scrapy.selector import Selector
from pprint import pprint
html="""<tbody>
                      <tr data-drupal-selector="edit-strings-996" class="odd">
                      <td><div id="edit-strings-996-original" class="js-form-item form-item js-form-type-item form-type-item js-form-item-strings-996-original form-item-strings-996-original form-no-label">
      <label for="edit-strings-996-original" class="visually-hidden">Source string (Built-in English)</label>
        Search
        </div>
</span></td>
                      <td><div class="js-form-item form-item js-form-type-textarea form-type-textarea js-form-item-strings-996-translations-0 form-item-strings-996-translations-0 form-no-label">
      <label for="edit-strings-996-translations-0" class="visually-hidden">Translated string (Español)</label>
        <div class="form-textarea-wrapper">
  <textarea lang="es" data-drupal-selector="edit-strings-996-translations-0" id="edit-strings-996-translations-0" name="strings[996][translations][0]" rows="1" cols="60" class="form-textarea resize-vertical">Search</textarea>
</div>

        </div>
</td>
                  </tr>
                      <tr data-drupal-selector="edit-strings-1176" class="even">
                      <td><div id="edit-strings-1176-original" class="js-form-item form-item js-form-type-item form-type-item js-form-item-strings-1176-original form-item-strings-1176-original form-no-label">
      <label for="edit-strings-1176-original" class="visually-hidden">Source string (Built-in English)</label>
        Search page
        </div>"""

# pprint(html)

data = Selector(text=html)
print(data.xpath('//div[normalize-space(text()[2]="Search")]/text()').get())
