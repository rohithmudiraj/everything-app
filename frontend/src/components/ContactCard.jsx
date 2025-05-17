const ContactCard = ({contact,idx})=> {
    return(
        <div key={idx} className="card mb-3 shadow-sm rounded">
          <div className="card-body">
            <h5 className="card-title"> {contact.name || ""}{contact.u_alias ? ` (${contact.u_alias})` : ""}</h5>
            <p className="card-text text-truncate" style={{ maxHeight: "4.5em" }}>
              {contact['short_description'] || ""}
            </p>
            <div className="row small text-secondary">
              <div className="col-md-6">
                <p><strong>Service Owner:</strong> {contact['owned_by'] || "-"}</p>
                <p><strong>Service Team:</strong> {contact['u_service_team'] || "-"}</p>
                <p><strong>Service Executive:</strong> {contact['u_service_executive'] || "-"}</p>
                <p><strong>Product Owner:</strong> {contact['u_product_owners'] || "-"}</p>
                <p><strong>Product Owner Executive:</strong> {contact['u_product_owner_exe'] || "-"}</p>
              </div>
              <div className="col-md-6">
                <p><strong>Problem Owner Group:</strong> {contact['u_problem_owner_group'] || "-"}</p>
                <p><strong>Problem Manager Group:</strong> {contact['u_problem_manager_group'] || "-"}</p>
                <p><strong>Managed By Group:</strong> {contact['managed_by_group'] || "-"}</p>
                <p><strong>Managed By:</strong> {contact['managed_by'] || "-"}</p>
                <p><strong>Approval Group:</strong> {contact['change_control'] || "-"}</p>
              </div>
            </div>
          </div>
        </div>

    )
}
 export default ContactCard;