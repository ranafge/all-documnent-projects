from scrapy.selector import Selector

html="""<table style="width: 100%">
      <thead>
        <tr>
          <td><!--Filename-->&nbsp;</td>
          <td class="hide-for-small">Version</td>
          <td class="hide-for-small">Language</td>
          <td>Size</td>
          <td class="hide-for-small">Uploaded</td>
        </tr>
      </thead>
      <tbody>



        <tr><td colspan="5"><h6>Specifications</h6></td></tr>
            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle; display: inline-block; background-image: url(&quot;https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png&quot;);" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png">
              <a href="/en/site_elements/elp-ww-ip-spec-sheet">ELP WW IP Spec Sheet</a>
              
              <div class="show-for-small">
                <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">
                <i>
                  version A, 
                  updated: Dec 02, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> A&nbsp;</td>
        <td class="text-center hide-for-small"> <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">&nbsp; </td>
        <td> 1010 KB </td>
        <td class="hide-for-small">Dec 02, 2020</td>



  </tr>




            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle; display: inline-block; background-image: url(&quot;https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png&quot;);" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png">
              <a href="/en/site_elements/martin-elp-ww-ip-acoustic-test-report">Martin ELP WW IP Acoustic Test Report</a>
              
              <div class="show-for-small">
                <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">
                <i>
                  version A, 
                  updated: Oct 15, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> A&nbsp;</td>
        <td class="text-center hide-for-small"> <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">&nbsp; </td>
        <td> 1.16 MB </td>
        <td class="hide-for-small">Oct 15, 2020</td>



  </tr>




        <tr><td colspan="5"><h6>Manuals</h6></td></tr>
            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle; display: inline-block; background-image: url(&quot;https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png&quot;);" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png">
              <a href="/en/site_elements/elp-ww-ip-user-manual-5791f4c2-3055-4f7a-ae18-100634f36417">ELP WW IP User Manual</a>
              
              <div class="show-for-small">
                <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">
                <i>
                  version C, 
                  updated: Oct 22, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> C&nbsp;</td>
        <td class="text-center hide-for-small"> <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">&nbsp; </td>
        <td> 1.85 MB </td>
        <td class="hide-for-small">Oct 22, 2020</td>



  </tr>




            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle; display: inline-block; background-image: url(&quot;https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png&quot;);" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png">
              <a href="/en/site_elements/martin-elp-ww-ip-user-manual">ELP WW IP User Manual</a>
              
              <div class="show-for-small">
                <img alt="de" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/de-3323814006fe6739493d27057954941830b59eff37ebaac994310e17c522dd57.png">
                <i>
                  version B, 
                  updated: Oct 06, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> B&nbsp;</td>
        <td class="text-center hide-for-small"> <img alt="de" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/de-3323814006fe6739493d27057954941830b59eff37ebaac994310e17c522dd57.png">&nbsp; </td>
        <td> 1.35 MB </td>
        <td class="hide-for-small">Oct 06, 2020</td>



  </tr>




            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle; display: inline-block; background-image: url(&quot;https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png&quot;);" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png">
              <a href="/en/site_elements/elp-ww-ip-user-manual">ELP WW IP User Manual</a>
              
              <div class="show-for-small">
                <img alt="fr" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/fr-79a39793efbf8217efbbc840e1b2041fe995363a5f12f0c01dd4d1462e5eb842.png">
                <i>
                  version B, 
                  updated: Oct 06, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> B&nbsp;</td>
        <td class="text-center hide-for-small"> <img alt="fr" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/fr-79a39793efbf8217efbbc840e1b2041fe995363a5f12f0c01dd4d1462e5eb842.png">&nbsp; </td>
        <td> 1.93 MB </td>
        <td class="hide-for-small">Oct 06, 2020</td>



  </tr>




        <tr><td colspan="5"><h6>Photometrics</h6></td></tr>
            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle; display: inline-block; background-image: url(&quot;https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png&quot;);" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png">
              <a href="/en/site_elements/elp-ww-ip-photometric-files">ELP WW IP Photometric Files</a>
              
              <div class="show-for-small">
                <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">
                <i>
                  version A, 
                  updated: Oct 06, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> A&nbsp; </td>
        <td class="text-center hide-for-small"> <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">&nbsp; </td>
        <td>
            5.77 MB
        </td>
        <td class="hide-for-small">Oct 06, 2020</td>



  </tr>




        <tr><td colspan="5"><h6>Illustrations</h6></td></tr>
            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle; display: inline-block; background-image: url(&quot;https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png&quot;);" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png">
              <a href="/en/site_elements/elp-ip-2d-dimensions-dwg">ELP IP - 2D Dimensions (DWG)</a>
              
              <div class="show-for-small">
                <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">
                <i>
                  version A, 
                  updated: Oct 06, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> A&nbsp; </td>
        <td class="text-center hide-for-small"> <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">&nbsp; </td>
        <td>
            8.3 MB
        </td>
        <td class="hide-for-small">Oct 06, 2020</td>



  </tr>




            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle; display: inline-block; background-image: url(&quot;https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png&quot;);" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png">
              <a href="/en/site_elements/elp-ip-2d-dimensions-pdf">ELP IP - 2D Dimensions (PDF)</a>
              
              <div class="show-for-small">
                <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">
                <i>
                  version A, 
                  updated: Oct 06, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> A&nbsp;</td>
        <td class="text-center hide-for-small"> <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">&nbsp; </td>
        <td> 792 KB </td>
        <td class="hide-for-small">Oct 06, 2020</td>



  </tr>




        <tr><td colspan="5"><h6>Symbols</h6></td></tr>
            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle; display: inline-block; background-image: url(&quot;https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png&quot;);" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png">
              <a href="/en/site_elements/autocad-2d-symbols">AutoCAD 2D Symbols</a>
              
              <div class="show-for-small">
                
                <i>
                  version 1.2, 
                  updated: Oct 22, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> 1.2&nbsp; </td>
        <td class="text-center hide-for-small"> &nbsp; </td>
        <td>
            2.26 MB
        </td>
        <td class="hide-for-small">Oct 22, 2020</td>



  </tr>




            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle" src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs=" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png">
              <a href="/en/site_elements/vectorworks-symbols-1af16ab9-771a-445f-9dd6-ba8a6d8a22b2">Vectorworks Symbols</a>
              
              <div class="show-for-small">
                
                <i>
                  version 2.9, 
                  updated: Jan 08, 2021
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> 2.9&nbsp; </td>
        <td class="text-center hide-for-small"> &nbsp; </td>
        <td>
            373 MB
        </td>
        <td class="hide-for-small">Jan 08, 2021</td>



  </tr>




            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle" src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs=" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png">
              <a href="/en/site_elements/autocad-3d-symbols-86527c19-1ef6-4d42-888a-d216232fe84b">AutoCAD 3D Symbols</a>
              
              <div class="show-for-small">
                
                <i>
                  version 1.2.5, 
                  updated: Jan 08, 2021
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> 1.2.5&nbsp; </td>
        <td class="text-center hide-for-small"> &nbsp; </td>
        <td>
            8.46 MB
        </td>
        <td class="hide-for-small">Jan 08, 2021</td>



  </tr>




        <tr><td colspan="5"><h6>CAD Drawings</h6></td></tr>
            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle" src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs=" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png">
              <a href="/en/site_elements/elp-3d-files">ELP IP 3D Files</a>
              
              <div class="show-for-small">
                <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">
                <i>
                  version A, 
                  updated: Oct 06, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> A&nbsp; </td>
        <td class="text-center hide-for-small"> <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">&nbsp; </td>
        <td>
            7.19 MB
        </td>
        <td class="hide-for-small">Oct 06, 2020</td>



  </tr>




        <tr><td colspan="5"><h6>Compliances</h6></td></tr>
            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle" src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs=" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png">
              <a href="/en/site_elements/elp-ip-listing-mark-verification-letter">ELP IP Listing Mark Verification Letter</a>
              
              <div class="show-for-small">
                <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">
                <i>
                  
                  updated: Jul 14, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> &nbsp;</td>
        <td class="text-center hide-for-small"> <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">&nbsp; </td>
        <td> 147 KB </td>
        <td class="hide-for-small">Jul 14, 2020</td>



  </tr>




            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle" src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs=" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png">
              <a href="/en/site_elements/elp-ip-supplier-s-declaration-of-conformity">ELP IP Supplier's Declaration of Conformity</a>
              
              <div class="show-for-small">
                <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">
                <i>
                  
                  updated: Jul 14, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> &nbsp;</td>
        <td class="text-center hide-for-small"> <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">&nbsp; </td>
        <td> 652 KB </td>
        <td class="hide-for-small">Jul 14, 2020</td>



  </tr>




            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle" src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs=" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png">
              <a href="/en/site_elements/martin-elp-ip-declaration-of-conformity">ELP IP Declaration of Conformity</a>
              
              <div class="show-for-small">
                <img alt="fr" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/fr-79a39793efbf8217efbbc840e1b2041fe995363a5f12f0c01dd4d1462e5eb842.png">
                <i>
                  
                  updated: Jul 14, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> &nbsp;</td>
        <td class="text-center hide-for-small"> <img alt="fr" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/fr-79a39793efbf8217efbbc840e1b2041fe995363a5f12f0c01dd4d1462e5eb842.png">&nbsp; </td>
        <td> 708 KB </td>
        <td class="hide-for-small">Jul 14, 2020</td>



  </tr>




            <tr class="download-item-row">
        <td>
          <div class="row">
            <div class="small-11 columns">
              <img style="vertical-align: middle" src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs=" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/pdf_17-c246fb20baff4fd092a406a45fe2aa40bfcc85a177b6a4e6ae1d29faca4f8f29.png">
              <a href="/en/site_elements/elp-ip-declaration-of-conformity">ELP IP Declaration of Conformity</a>
              
              <div class="show-for-small">
                <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">
                <i>
                  
                  updated: Jul 14, 2020
                </i>
              </div>
            </div>
            <div class="small-1 columns">
            </div>
          </div>
        </td>
        <td class="text-center hide-for-small"> &nbsp;</td>
        <td class="text-center hide-for-small"> <img alt="en" src="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/flags/en-34c5b8d249866c95721154e6f54863a060e3f86b8861cfe2f093bd479105a487.png">&nbsp; </td>
        <td> 715 KB </td>
        <td class="hide-for-small">Jul 14, 2020</td>



  </tr>




        <tr><td colspan="5"><h6>Firmware</h6></td></tr>
            <tr class="download-item-row">
      <td>
        <div class="row">
          <div class="small-11 columns">
            <img style="vertical-align: middle" src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs=" data-original="https://22b375f28cb4a3978d5e-76f43cbbcaa8592c8e9d0bfe87e3817b.ssl.cf2.rackcdn.com/assets/icons/download_17-78b2535bf0107dd7e9920fc8283e4a8a0f28d7451873aabe3ed1de61d4f7f3db.png">
            <a href="https://www.martin.com/firmware">ELP WW IP - Firmware</a>
            <div class="show-for-small">
              
              <i>
                version 1.0.04, 
                updated: Jan 18, 2021
              </i>
            </div>
          </div>
          <div class="small-1 columns text-right">
          </div>
        </div>
      </td>
      <td class="text-center hide-for-small">
          1.0.04
        &nbsp;</td>
      <td class="text-center hide-for-small"> &nbsp; </td>
      <td>
      </td>
      <td class="hide-for-small">Jan 18, 2021</td>

  </tr>


      </tbody>
    </table>"""

data = Selector(text=html)
 # select all tr having a count() of td > 2
print(data.xpath('//tr[count(td)<5]//text()').getall())
