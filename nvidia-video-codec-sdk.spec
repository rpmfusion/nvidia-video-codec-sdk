%global src_name Video_Codec_SDK

Name:           nvidia-video-codec-sdk
Version:        7.1.9
Release:        1%{?dist}
Summary:        Hardware accelerated video encode and decode

License:        Redistributable, no modification permitted
URL:            https://developer.nvidia.com/nvidia-video-codec-sdk
# Needs registration at upstream URL and manual download
Source0:        %{src_name}_%{version}.zip

BuildArch:      noarch

%description
The Video Codec SDK includes a complete set of high-performance tools, 
samples and documentation for hardware accelerated video encode and decode. 

%package -n nvenc-devel
Summary:        Header for nvEncode API
License:        MIT/X11 (BSD like)

%description -n nvenc-devel
The NVIDIA Encoder (NVENC) API enables software developers to access the
high-performance hardware H.264 and HEVC (H.265) video encoder in Kepler and
Maxwell class NVIDIA GPUs. NVENC provides high-quality video encoding that is
faster and more power efficient in comparison to equivalent CUDA-based or
CPU-based encoders. By using dedicated hardware for the video encoding task, the
GPU CUDA cores and/or the CPU are available for other compute-intensive tasks.
NVENC on GeForce hardware can support a maximum of 2 concurrent streams per
system. NVENC for GRID, Tesla and certain Quadro GPUs (see below) can support as
many streams as possible up to maximum NVENC encoder rate limit and available
video memory. 

%prep
%setup -q -n %{src_name}_%{version}
rm doc/NVDEC_*

%build
# Nothing to do

%install
install -m 644 -p -D Samples/common/inc/nvEncodeAPI.h \
    %{buildroot}%{_includedir}/nvenc/nvEncodeAPI.h

%files -n nvenc-devel
%doc doc/*.pdf
%license LicenseAgreement.pdf
%{_includedir}/nvenc/


%changelog
* Thu Dec 01 2016 leigh scott <leigh123linux@googlemail.com> - 7.1.9-1
- update to 7.1.9

* Wed Aug 03 2016 Leigh Scott <leigh123linux@googlemail.com> - 7.0.1-1
- first build

